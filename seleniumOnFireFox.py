from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get('https://google.com')
driver.maximize_window()
title = driver.title  # returns the title of the page
print(title)
assert "Selenium" in title  # verify if the title name is e.g.(selenium)

driver.find_element(By.CSS_SELECTOR, '#APjFqb')
