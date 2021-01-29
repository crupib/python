from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.amazon.com/")
ele = driver.find_element_by_name("field-keywords")
time.sleep(1)
ele.clear()
ele.send_keys("Quantum Physics")
ele.send_keys(Keys.RETURN)
driver.close()
time.sleep(5)
