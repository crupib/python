from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://sbasu.pythonanywhere.com/tastyFoodApp/")
print("The url is ", driver.current_url) 
expected_val = "Tasty Home Food Delivery Service"
received_title = driver.title
if (received_title == expected_val):
   print("The title matches")
else:
   print("The title does not match")
print("The received title is ", received_title)
try:
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable
              ((By.LINK_TEXT, "Create New Profile"))
              ) 
    element.click()
    
    # Keep the browser open for 10 seconds
    time.sleep(2)
    firstName = driver.find_element(By.ID,'id_firstName')
    firstName.send_keys("Kia")
    val1 = firstName.get_attribute('value')
    print("The first name is", val1)
    time.sleep(2)
    lastName = driver.find_element(By.ID,'id_lastName')
    lastName.send_keys("Taco")
    time.sleep(2)
    username = driver.find_element(By.ID,'id_username')
    username.send_keys("KiaTaco")
    entered_username = username.get_attribute('value')
    username_input = driver.find_element(By.XPATH, '//input[@id="id_username"]')
    displayed_username = username_input.get_attribute('value')
    if (entered_username == displayed_username):
       print("The username matches")
    else:
       print("The username does not match")
    time.sleep(2)
    password = driver.find_element(By.ID,'id_password')
    password.send_keys("Kia23")
    time.sleep(2)
    state = Select(driver.find_element(By.ID,'id_state'))
    state.select_by_visible_text('Texas')
    time.sleep(2)
    fee = Select(driver.find_element(By.ID,'id_fee'))
    fee.select_by_visible_text('$150 : Gold')
    time.sleep(2)
    button = driver.find_element(By.ID,'js_button')
    button.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    received_intro = driver.find_element(By.CLASS_NAME, 'text')
    received_content = received_intro.text
    expected_intro = "Greetings, Please fill the form below to get enrolled into the World's Best Home Food Delivery Service"
    if received_content == expected_intro:
       print("The text matches")
    else:
       print("The text does not match")
    time.sleep(10)
finally:
    driver.quit()  # Close the browser after the delay
