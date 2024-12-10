import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("http://localhost:8000/index.html")
element = driver.find_element(By.CLASS_NAME,'content')
time.sleep(3)
print(element.text)
driver.close()
driver.quit()
