import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Firefox()

try:
    # Open the webpage
    driver.get("https://www.geeksforgeeks.org/")
    
    # Wait for the element to appear
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "HomePageSearchContainer_homePageSearchContainer_container_input__1LS0r"))
    )
    
    # Input text into the element
    search_box.send_keys("python")
    time.sleep(5)    
    search_box.send_keys(Keys.RETURN) 
    time.sleep(5)    
    
except Exception as e:
    print(f"Error occurred: {e}")
    print(driver.page_source)  # Print the page source for debugging
    
finally:
    driver.quit()
