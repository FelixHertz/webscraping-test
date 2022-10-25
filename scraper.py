from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument ("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.set_capability("browserVersion", "104.0.5112.79")
chrome_options.set_capability("platformName", "linux")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
##driver = webdriver.Chrome(service=Service('./chromedriver'), options=chrome_options)
driver.get("http://www.google.com/")
print(driver.page_source)
        
