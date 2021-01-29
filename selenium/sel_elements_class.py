from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome()
driver.get("https://www.pluralsight.com/")
ele = driver.find_element_by_class_name("button--secondary--white")
ele.click()
time.sleep(5)
driver.quit()
