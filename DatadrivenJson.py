import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

with open('TextingData2 copy.json', 'r', encoding='utf-8-sig') as file:
    test_data = json.load(file)

for data in test_data['users']:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url="https://www.saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.ID, "user-name").send_keys(data['username'])
    driver.find_element(By.ID, "password").send_keys(data['password'])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    driver.quit()
