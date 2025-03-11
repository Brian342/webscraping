import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.execute_script("window.scrollTo(0,900)")  # used to scroll the page
driver.get(
    url="https://dph.illinois.gov/topics-services/diseases-and-conditions/hiv-aids/hiv-surveillance/update-reports/2023/february.html")

Table_details = driver.find_element(By.XPATH, "//*[@id='DataTables_Table_1']")
rows = Table_details.find_elements(By.XPATH, ".//tbody/tr")

data = []  # create an empty list
for _ in rows:
    cells = _.find_elements(By.XPATH, ".//td")
    row_data = [cell.text for cell in cells]
    data.append(row_data)

for row in data:
    print(row)

if __name__ == "__main__":
    driver.quit()

with open('St. Clair County Breakdown.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Health Department", "Cases Diagnosed as of 2/28/2023", "Cumulative Cases Diagnosed Since 2016"])
    writer.writerows(data)
print("Data written successfully")