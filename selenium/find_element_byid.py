import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox()
try:
  driver.get("http://localhost:8000/index.html")
  try:
    element = driver.find_element(By.NAME,'username')
    time.sleep(3)
    print(element.get_attribute('value'))
  except NoSuchElementException:
    print("Element not found")
finally:
  driver.close()
  driver.quit()
