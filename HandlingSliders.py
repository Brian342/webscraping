import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/horizontal_slider")
slider = browser.find_element(By.XPATH, "//input[@type='range']")
action = ActionChains(browser)
action.click_and_hold(slider).move_by_offset(100, 0).release().perform()  # performing the action of sliding an element
# X-offset the movement of the mouse
# Y-offset the last point of the mouse
time.sleep(10)
browser.quit()