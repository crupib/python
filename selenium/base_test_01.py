from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set the correct path to the Firefox binary
options = Options()
options.binary_location = '/Applications/Firefox.app/Contents/MacOS/firefox'

# Specify the path to geckodriver using the Service class
service = Service(executable_path='/usr/local/bin/geckodriver')

# Initialize the Firefox WebDriver with the service and options
driver = webdriver.Firefox(service=service, options=options)

# Open the URL
driver.get("http://google.com")

# Find the search box using the By class and search for a term
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Mayank Johri")

# Submit the form
search_box.send_keys(Keys.RETURN)

# Optional: Close the browser
# driver.quit()

