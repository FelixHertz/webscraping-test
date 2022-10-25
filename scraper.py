from bs4 import BeautifulSoup
import requests
import re
import mysql.connector


mydb = mysql.connector.connect(host="h1.host.filess.io", user="dudenv2_bystreamwe", passwd="239848e4ad651c7b21981c6cd1fea4bf6ec5c444", database="dudenv2_bystreamwe", port="3307")
mycursor = mydb.cursor()

def add_data(wort, gebrauch):
    try:
        sql = "INSERT INTO wort_erg (wort, gebrauch) VALUES (%s, %s)"
        val = (wort, gebrauch)
        mycursor.execute(sql, val)
        mydb.commit()
    except:
                print("Error")

def add_data_other(wort, gebrauch):
    try:
        sql = "INSERT INTO other (wort, gebrauch) VALUES (%s, %s)"
        val = (wort, gebrauch)
        mycursor.execute(sql, val)
        mydb.commit()
    except:
                print("Error")

words = ['a']

with open('deutsch.txt', mode='r', encoding='utf-8') as fp:
    contents = fp.read().splitlines()
    for i in contents:
        words.append(i)


header = {"User-Agent":"Custom"}

def scrape():
    for entry in words:
        try:
            url = f"https://www.duden.de/rechtschreibung/{entry}"

            print(url)

            result = requests.get(url, headers=header)
            doc = BeautifulSoup(result.text, "html.parser")
            
            search = doc.find(text=re.compile('Gebrauch:')).parent.find_next('dd')
            extract = search.text
            print(extract)

            if extract == 'bildungssprachlich':
                add_data(entry, 'bildungssprachlich')
            if extract == 'gehoben':
                add_data(entry, 'gehoben')
            if extract != 'bildungssprachlich':
                if extract != 'gehoben':
                    add_data_other(entry, extract)

        except:
            print("")
scrape()

