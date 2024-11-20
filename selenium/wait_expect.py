import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://sbasu.pythonanywhere.com/tastyFoodApp/create")
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
element = wait.until(EC.presence_of_element_located((By.ID,"id_firstName")))
element.send_keys("KiaTaco")
time.sleep(10)
driver.quit()  # Close the browser after the delay
