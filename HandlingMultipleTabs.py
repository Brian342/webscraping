import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
url = "https://www.selenium.dev/"
driver.get(url)
driver.maximize_window()
time.sleep(10)
driver.switch_to.new_window()  # opens a new window tab
driver.get('https://playwright.dev/')

# counts the total number of tabs on the browser
number_of_tabs = len(driver.window_handles)
print(f"number of tabs: {number_of_tabs}")

# returns the tabs values
tabs_value = driver.window_handles  # returns unique element of the tabs
print(f"tabs_value: {tabs_value}")

# returns the current tab value
current_tab = driver.current_window_handle  # returns the value of the current tab
print(f"current_value: {current_tab}")

# returns the current tab
driver.find_element(By.CSS_SELECTOR, ".getStarted_Sjon").click()
time.sleep(10)

firstTab = driver.window_handles[1]  # second tab element array
print(firstTab)

if current_tab != firstTab:
    driver.switch_to.window(firstTab)
driver.find_element(By.XPATH, "//span[normalize-space()='Downloads']").click()

time.sleep(10)