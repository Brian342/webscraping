import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get('https://the-internet.herokuapp.com/nested_frames')
driver.maximize_window()

#  Switching to top frame

driver.switch_to.frame("frame-top")

#  Switching to Middle Frame

driver.switch_to.frame("frame-middle")

content = driver.find_element(By.ID, "content").text
print(f"Content: {content}")

#  switch to default content
driver.switch_to.default_content()

#  switching to the bottom frame
driver.switch_to.frame("frame-bottom")
contentBottom = driver.find_element(By.TAG_NAME, "body").text
print(f"Content on bottom-frame {contentBottom}")

time.sleep(10)
driver.quit()