from datetime import datetime, timedelta
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Safari()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()
driver.find_element(By.ID, "datepicker2").click()
time.sleep(5)
current_date = datetime.now()  # returns the current time
print(current_date)

next_day = current_date + timedelta(days=1)  # Adds a day
print(next_day)

Next_day = (str(next_day.day))  # returns the next day of the time
print(Next_day)

current_month = datetime.now().month  # returns the current month of the time
current_year = current_date.year  # returns the current year

next_month = (current_month % 12) + 1  # returns the next month
next_month_year = f"{next_month}/{current_year}"

month_dropdown = driver.find_element(By.CSS_SELECTOR, "select[title='Change the month']")
select = Select(month_dropdown)
select.select_by_value(str(next_month_year))  # selects the month on the dropdown

Year_Dropdown = driver.find_element(By.CSS_SELECTOR, "select[title='Change the year']")
select = Select(Year_Dropdown)
select.select_by_visible_text("2025")

driver.find_element(By.LINK_TEXT, Next_day).click()
time.sleep(10)
