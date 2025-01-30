from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.options import

driver = webdriver.Safari()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)

dropdown_element = driver.find_element(By.ID, "dropdown")

# ----------------------------------------------------------------------------------
# This code checks on the dropdown if the target_value is present then selects it on the browser
target_value = "Option 2"
select = Select(dropdown_element)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected Option is {target_value}")
        break
    else:
        print(f"Option '{target_value}' not found")

# ---------------------------------------------------------------------------------
# select = Select(dropdown_element)
#
# counting and verify how many elements are on the dropdown options
# option_count = len(select.options)
#
# expected_count = 3
# if option_count == expected_count:
#     print ('Test case passed. count is correct')
# else:
#     print ('Test case Failed. count is incorrect')

# ----------------------------------------------------------------------------------
# Select the value by visible text,
# select the value by index,
# select the option by using a value

# select.select_by_visible_text("Option 2") # selects the text using visible text from the dropdown option
# select.select_by_index(1)  #  selects the text on the dropdown using index
# select.select_by_value("1")  #  selects the text on the dropdown using value attribute

