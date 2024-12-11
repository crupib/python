import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox()
try:
  driver.get("http://localhost:8000/index.html")
  try:
    element = driver.find_element(By.XPATH,'/html/body/form[1]')
    time.sleep(3)
    print(element)
    element2 = driver.find_element(By.XPATH,'//form[1]')
    print(element2)
  except NoSuchElementException:
    print("Element not found")
finally:
  driver.close()
  driver.quit()
