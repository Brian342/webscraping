import time

from selenium import webdriver
# from selenium.webdriver.chrome.options  # import Options for chrome
# from selenium.webdriver.firefox.options import Options # for firefox browser
from selenium.webdriver.safari.options import Options  # for safari window


safari_option = Options()
safari_option.add_argument("--Private Browsing")
# use "--incognito" for chrome
# use "--private" for firefox

driver = webdriver.Safari(options=safari_option)
driver.maximize_window()
time.sleep(10)
driver.get("https://dph.illinois.gov/topics-services/diseases-and-conditions/hiv-aids/hiv-surveillance/update-reports/2023/february.html")
driver.quit()