from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()  # maximizes the browser page
# driver.minimize_window()  # minimizes the browser page
# driver.fullscreen_window()  # makes the browser full screen
time.sleep(10)
driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()
time.sleep(10)
driver.back()  # previous page
time.sleep(10)
driver.forward()  # forward the page
driver.refresh()  # refreshes the page
time.sleep(10)
driver.close()
