import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://www.globalsqa.com/demo-site/datepicker/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//div[@class='attention closable'][normalize-space()='Pick a date by clicking on the text box.']").click()
time.sleep(5)
# Switching no the frame
frameLo = driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(frameLo)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#datepicker").click()

current_date = datetime.now()  # returns the current time value

next_date = current_date + timedelta(days=1)  # current date plus one day meaning today plus tomorrow

formatted_date = next_date.strftime("%m/%d/%y")

driver.find_element(By.CSS_SELECTOR, "#datepicker").send_keys(formatted_date + Keys.TAB)
time.sleep(5)
driver.quit()
