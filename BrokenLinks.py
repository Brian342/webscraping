from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Safari()
url = "https://jqueryui.com/"
driver.get(url)
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total no of links on page, {len(all_links)} ")

for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken Link: {href}(status code: {response.status_code})")

driver.quit()
