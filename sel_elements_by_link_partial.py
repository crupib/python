from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
chromeOptions = Options()
#chromeOptions.add_argument("--kiosk")
driver = webdriver.Chrome()
#driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.amazon.com/")
ele_link = driver.find_element_by_partial_link_text("New")
ele_link.click()
time.sleep(5)
driver.quit()
