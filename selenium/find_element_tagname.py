import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("http://localhost:8000/index.html")
element = driver.find_element(By.TAG_NAME,'h1')
time.sleep(3)
print(element.tag_name)
driver.close()
driver.quit()
