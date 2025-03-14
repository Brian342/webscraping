# web scrapping using selenium
# Task extrack the February 2023 Hiv surveillance update report
import time
import csv
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector

#
driver = webdriver.Chrome()
driver.fullscreen_window()
driver.get(
    "https://dph.illinois.gov/topics-services/diseases-and-conditions/hiv-aids/hiv-surveillance/update-reports/2023/february.html")

# waiting for table to load
Table_wait = WebDriverWait(driver, 10)
Table = Table_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table")))

# getting the number of pages
table_text = driver.find_element(By.XPATH, "//div[contains(text(),'Showing 1 to 10')]").text
start_index = table_text.find("of") + 3
end_index = table_text.find("entries") - 1
pages = int(table_text[start_index:end_index])
print(f"No of entries: {pages}")

data = []
for page in range(1, pages + 1):
    try:
        Table = Table_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table")))

        # find elements on the table
        row = Table.find_elements(By.XPATH, ".//tbody/tr")
        for _ in row:
            cells = _.find_elements(By.XPATH, ".//td")
            row_data = [cell.text for cell in cells]
            data.append(row_data)

        # check if the last data is on the table
        if any("Illinois" in row for row in data):
            break

        # next page
        next_element = driver.find_element(By.XPATH, "//a[contains(@class, 'paginate_button next')]")
        if "disabled" in next_element.get_attribute("class"):
            break
        next_element.click()

        time.sleep(5)
    except NoSuchElementException as e:
        print(f'Error: {e}')
        break

for row in data:
    print(row)

if __name__ == "__main__":
    driver.quit()

# with open('February 2023 Hiv surveillance update report.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     if data:
#         writer.writerow(["County", "Cases Diagnosed as of 2/28/2023", "Cumulative Cases Diagnosed Since 2016", "2016-2023 HIV Diagnosis Rate"])
#     writer.writerows(data)
# 
# print('Data written successfully!!')


conn = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="Illinois",
    password="",
    database="ILLINOIS_DEPARTMENT_OF_PUBLIC_HEALTH"
)
cursor = conn.cursor()

# create a table to store the data
cursor.execute('''
CREATE TABLE IF NOT EXISTS February_2023_Surveillance_Update_Report (
    id INT AUTO_INCREMENT PRIMARY KEY,
    County VARCHAR(255),
    Cases_Diagnosed_as_of_2/28/2023 INT,
    Cumulative_Cases_Diagnosed_Since_2016 INT,
    2016-2023 HIV Diagnosis Rate DOUBLE
    )
    ''')

# insert the scraped data into the table
for row in data:
    cursor.execute('''
    INSERT INTO February_2023_Surveillance_Update_Report 
    (County, Cases Diagnosed as of 2/28/2023, Cumulative Cases Diagnosed Since 2016, 2016-2023 HIV Diagnosis Rate)
    VALUES (%s ,%s, %s, %s)
    ''', (row[0], row[1], row[2], row[3]))  # adjusting indices based on your data structure

# commit the transaction and close the connection
conn.commit()
conn.close()

print('Data has been saved to the MYSQL Database successfully')
