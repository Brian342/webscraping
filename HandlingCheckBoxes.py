import time
import tkinter as tk
from tkinter import simpledialog

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # used to scroll the page of the site

Root = tk.Tk()
Root.withdraw()

expected_checked_count = simpledialog.askinteger(title="CheckBox Count",
                                                 prompt="Enter the expected_checked_count: ")
print("expected_checked_count: ", expected_checked_count)

checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
# iterates through the checkboxes
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

checked_count = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1

if checked_count == expected_checked_count:
    print('Checkbox count verified')
else:
    print('Checkbox count mismatch')
time.sleep(5)
driver.close()

# driver.find_element(By.XPATH, "//label[normalize-space()='Sunday']").click()  # checks the first checkbox

# start at 2.03.05 selenium webdriver
