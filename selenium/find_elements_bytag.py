import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox()
try:
  driver.get("http://localhost:8000/index.html")
  try:
    element = driver.find_elements(By.TAG_NAME,'a')
    print(f"Number of elements: {len(element)}")
    time.sleep(3)
    for element in element:
      print(element.get_attribute('href'))
  except NoSuchElementException:
    print("Element not found")
finally:
  driver.close()
  driver.quit()
