import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://www.pluralsight.com/")
time.sleep(5)
driver.quit()
