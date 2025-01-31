import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# alertButton = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
# alertButton.click()  # clicks the alert pop up message
#
# alert = driver.switch_to.alert  # switches to the alert pop-up message
# alertText = alert.text
# print(alertText)  # returns the alert message to user
# time.sleep(5)
# alert.accept()  # clicks the alert button on the pop-up message

# --------------------------------------------------------------------------------------------------------------------
# Alert message with 2 options
# alertButton = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
# alertButton.click()  # clicks the alert pop up message
# alertConfirm = driver.switch_to.alert
# time.sleep(5)
# alertConfirm.dismiss()

# ---------------------------------------------------------------------------------------------------------------------
# alert message with user prompt
alertButton = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
alertButton.click()
AlertUser = driver.switch_to.alert
time.sleep(5)
AlertUser.send_keys("This is selenium with python tutorial on handling alerts")
AlertUser.accept()
time.sleep(10)


time.sleep(10)
