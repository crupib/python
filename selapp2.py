import geckodriver_autoinstaller
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
geckodriver_autoinstaller.install()  
with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://seleniumhq.github.io")
    # Setup wait for later
    wait = WebDriverWait(driver, 10)
    # Store the ID of the original window
    original_window = driver.current_window_handle
    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1
    # Click the link which opens in a new window
    wait.until(EC.number_of_windows_to_be(1))
    driver.find_element(By.LINK_TEXT, "About").click()
    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(1))
    driver.find_element(By.LINK_TEXT, "Ecosystem").click()
    wait.until(EC.number_of_windows_to_be(1))
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    time.sleep(5)
