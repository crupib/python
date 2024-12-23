import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox()
try:
  driver.get("https://www.geeksforgeeks.org")
  try:
#    element = driver.find_element(By.ID,'comp')
    element = driver.find_element(By.CLASS_NAME, "HomePageSearchContainer_homePageSearchContainer_container_input__1LS0r")
    time.sleep(3)
    print(element.get_attribute("class"))
  except NoSuchElementException:
    print("Element not found")
finally:
  driver.close()
  driver.quit()
