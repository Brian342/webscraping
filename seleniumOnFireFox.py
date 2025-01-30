from selenium import webdriver

browser = webdriver.Safari()
browser.get('https://selenium.dev/')
browser.maximize_window()
title = browser.title  # returns the title of the page
print(title)
assert "Selenium" in title  # verify if the title name is e.g.(selenium)
