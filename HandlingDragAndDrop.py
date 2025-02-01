import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browsers = webdriver.Chrome()
browsers.maximize_window()
browsers.get("https://the-internet.herokuapp.com/drag_and_drop")
source_element = browsers.find_element(By.ID, "column-a")
time.sleep(5)
destination_element = browsers.find_element(By.ID, "column-b")
time.sleep(5)
action = ActionChains(browsers)
action.drag_and_drop(source_element, destination_element).perform()
time.sleep(10)
browsers.quit()
