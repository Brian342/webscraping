import time

from selenium import webdriver
import csv

from selenium.webdriver.common.by import By

csv_file = 'TextingData2.csv'

# reading the data from the csv file
test_date = []
with open(csv_file, 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row = {('username' if k == "\ufeffusername" else k): v for k, v in row.items()}
        test_date.append(row)
print(test_date)

for data in test_date:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url="https://www.saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.ID, "user-name").send_keys(data['username'])
    driver.find_element(By.ID, "password").send_keys(data['password'])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    driver.quit()
