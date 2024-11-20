from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
class BasePage:
  def __init__(self,driver):
    self.driver = driver
  def set_element_id(self,locator_value,input_value):
    driver = self.driver
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, locator_value)))
    element.click()
    element.send_keys(input_value)
