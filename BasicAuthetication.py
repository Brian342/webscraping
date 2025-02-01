import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# credentials
username = 'admin'
password = 'admin'
# connection
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url="https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
driver.quit()

# ----------------------------------------------------------------------------------------
# https://username:password@domain/path - allows one to access an authentication website

