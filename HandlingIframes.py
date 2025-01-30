import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Safari()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
time.sleep(10)

iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "mce_0_ifr"))
)
driver.switch_to.frame(iframe)

time.sleep(10)
# executing a JavaScript code to bypass the read-only mode
driver.execute_script("document.designMode = 'on';")  # Enables editing

time.sleep(10)

text_editor = driver.find_element(By.ID, "tinymce")
text_editor.clear()
text_editor.send_keys("Hey... I am the Best In the world!!")

driver.switch_to.default_content()  # switches back to the main content page of the HTML

time.sleep(10)