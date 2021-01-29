from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
chromeOptions = Options()
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
ele_link = driver.find_element_by_link_text("Gift Cards")
ele_link.click()
time.sleep(5)
driver.quit()
