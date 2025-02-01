import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Resizable.html")
resizeable_element = driver.find_element(By.CSS_SELECTOR,
                                         ".ui-resizable-handle.ui-resizable-se.ui-icon.ui-icon-gripsmall-diagonal-se")
initial_element_size = driver.find_element(By.CSS_SELECTOR, "#resizable")
initial_size = initial_element_size.size  # returns the size of the object
print(f"initial_size: {initial_size}")
time.sleep(10)
action = ActionChains(driver)
action.click_and_hold(resizeable_element).move_by_offset(100, 100).release().perform()
time.sleep(10)
final_size = initial_element_size.size
print(f"final_size: {final_size}")
driver.quit()
