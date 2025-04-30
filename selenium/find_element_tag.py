import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox()
try:
  driver.get("http://localhost:8000/index.html")
  try:
    element = driver.find_element(By.TAG_NAME,'h1')
    time.sleep(3)
    print(element.text)
  except NoSuchElementException:
    print("Element not found")
finally:
  driver.close()
  driver.quit()
