import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox()
try:
  driver.get("https://www.geeksforgeeks.org")
  try:
#    element = driver.find_element(By.ID,'comp')
    element = driver.find_element(By.ID, "__NEXT_DATA__")
    time.sleep(3)
    print(element.get_attribute('type'))
  except NoSuchElementException:
    print("Element not found")
finally:
  driver.close()
  driver.quit()
