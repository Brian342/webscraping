# Wait = WebDriverWait(driver, 10)
# Table = Wait.until(EC.presence_of_all_elements_located((By.ID, "DataTables_Table_0")))
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.execute_script("window.scrollTo(0,900)")  # used for scrolling a website horizontal, vertical

driver.get(
    url="https://dph.illinois.gov/topics-services/diseases-and-conditions/hiv-aids/hiv-surveillance/update-reports/2023/february.html")

# waiting for table to load
table_details = driver.find_element(By.ID, "DataTables_Table_0")
rows = table_details.find_elements(By.XPATH, ".//tbody/tr")
row_count = len(rows)

data = []
for _ in rows:
    cells = _.find_elements(By.XPATH, ".//td")
    row_data = [cell.text for cell in cells]
    data.append(row_data)

# print in a single row
for row in data:
    print(row)
if __name__ == "__main__":
    driver.quit()

with open('CookCountyBreakdown.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Health Department', 'Cases Diagnosed as of 2/28/2023', 'Cumulative Cases Diagnosed Since 2016'])
    writer.writerows(data)
print('Data written successfully')
