import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("http://localhost:8000/index.html")
element = driver.find_element(By.NAME,'username')
element.clear()
element.send_keys("bill Crupi")
login_form = driver.find_element(By.XPATH,"//form[1]/input[1]")
time.sleep(3)
#login_form = driver.find_element(By.XPATH,"/html/body/form[1]/input[1]")
login_form.clear()
time.sleep(3)
href_test = driver.find_element(By.LINK_TEXT,'Continue')
href_test.click()
time.sleep(3)
driver.back()
time.sleep(3)
href_partial = driver.find_element(By.PARTIAL_LINK_TEXT,'Can')
href_partial.click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.close()
driver.quit()
