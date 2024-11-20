import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import createNewProfile
class Testing(unittest.TestCase):
  def setUp(self):
     self.driver = webdriver.Chrome()
     self.driver.maximize_window()
     self.driver.get("http://sbasu.pythonanywhere.com/tastyFoodApp/create")
  def test_CreatePage(self):
     driver = self.driver
     home = createNewProfile.CreateNewProfile(driver)
     title = home.get_title()
     self.assertEqual("Create New Profile - Tasty Home Food Delivery Service",title,"title did not match")
     intro = home.get_intro_text()
     self.assertEqual("Greetings, Please fill the form below to get enrolled into the World's Best Home Food Delivery Service",intro,"Intro did did not match")
     home.firstName("kia456")
  def tearDown(self):
     self.driver.quit()
if __name__ == '__main__':
   unittest.main()
     
     
