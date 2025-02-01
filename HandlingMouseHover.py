import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Safari()
browser.maximize_window()
browser.get("https://demo.automationtesting.in/Datepicker.html")
action = ActionChains(browser)

hover_element = browser.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']")
time.sleep(10)
action.move_to_element(hover_element).perform()  # uses the mouse to hover over the element
browser.find_element(By.XPATH, "//a[normalize-space()='Frames']").click()
time.sleep(10)

