from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
chromeOptions = Options()
#chromeOptions.add_argument("--kiosk")
driver = webdriver.Chrome()
#driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.amazon.com/")
ele_link = driver.find_element_by_link_text("Sign in")
ele_link.click()
ele = driver.find_element_by_name("email")
time.sleep(1)
ele.clear()
ele.send_keys("xxxx@yyyyy.com")
ele.send_keys(Keys.RETURN)
ele = driver.find_element_by_name("password")
ele.send_keys("*******")
ele.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()
