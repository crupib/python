from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
driver = webdriver.Chrome()
driver.get("https://www.python.org/")
ele = driver.find_element_by_id("id-search-field")
time.sleep(1)
ele.clear()
ele.send_keys("lists")
ele.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()
