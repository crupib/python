from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.headless = True
browser = webdriver.Chrome(options=options)
browser.get("https://www.unixtimestamp.com/")
timestamp = browser.find_element_by_css_selector('h3.text-danger:nth-child(3)')
print('Current timestamp: %s' % (timestamp.text.split(' ')[0]))
browser.close()
