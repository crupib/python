from selenium import webdriver
from locators import HomePageLocators
from selenium.webdriver.common.by import By

class HomePage():
  def __init__(self,driver):
    self.driver = driver
  def test_title(self):
    get_title = self.driver.title
    return get_title
  def test_heading(self):
    get_heading = self.driver.find_element(By.XPATH, HomePageLocators.heading_xpath)
    return get_heading.text
  def test_link(self):
    get_link = self.driver.find_element(By.LINK_TEXT, HomePageLocators.link_text_1)
    return get_link
