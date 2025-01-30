# from seleniumwire import webdriver  # Import Selenium Wire
#
# # Proxy details
# PROXY_HOST = "brd.superproxy.io"
# PROXY_PORT = "9515"
# PROXY_USER = "brd-customer-hl_d35b3d9a-zone-website"
# PROXY_PASS = "k84kvx52quc7"
#
# # Configure proxy settings
# options = {
#     'proxy': {
#         'http': f'http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}',
#         'https': f'https://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}',
#         'no_proxy': 'localhost,127.0.0.1'
#     }
# }
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # used for searching elements on the website
from selenium.webdriver.common.keys import Keys  # keys to enter a search
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import \
    expected_conditions as EC  # used to wait presence of an element before proceeding
import time

service = Service(executable_path="chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get('https://www.kilimall.co.ke/')


# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "input"))
# )  # if after 5 seconds the element does not exist crash the program

input_element = driver.find_element(By.CLASS_NAME, "van-field__body")
input_element.clear()
input_element.send_keys("Samsung" + Keys.ENTER)

# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Samsung "))
# )
#
# link = driver.find_element(By.PARTIAL_LINK_TEXT, "Samsung ")
# link.click()

time.sleep(10)
driver.quit()
