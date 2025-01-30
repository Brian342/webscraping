import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Safari()
browser.get("https://cosmocode.io/automation-practice-webtable/")
browser.maximize_window()
browser.execute_script("window.scrollTo(0,700)")  # used for scrolling a website horizontal, vertical
table = browser.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows)
print(f"Row_count: {row_count}")
target_value = "Kenya"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if target_value in cell.text:
            print(f"Found Value {target_value}")
            found = True
            break
    if found:
        break
if not found:
    print(f"Target value: '{target_value}' not found")
time.sleep(10)
