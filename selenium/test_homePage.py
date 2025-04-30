import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import homePage
class Testing(unittest.TestCase):
  def setUp(self):
     self.driver = webdriver.Chrome()
     self.driver.maximize_window()
     self.driver.get("http://sbasu.pythonanywhere.com/tastyFoodApp/")
  def test_HomePage(self):
     driver = self.driver
     home = homePage.HomePage(driver)
     title = home.test_title()
     self.assertEqual("Tasty Home Food Delivery Service",title,"title did not match")
     heading = home.test_heading()
     self.assertEqual("Tasty Home Food Delivery Service",heading,"Heading did did not match")
     link_1 = home.test_link()
     self.assertTrue(link_1.is_enabled(), "Button is not enabled")
     link_1.click()
  def tearDown(self):
     self.driver.quit()
if __name__ == '__main__':
   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/williamcrupi/Documents/github/python/selenium'))
