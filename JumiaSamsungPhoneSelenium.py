from selenium.webdriver.common.by import By
from seleniumbase import BaseCase
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

from seleniumwire import webdriver

# Path to the adblock extension (either .crx file or unpacked extension folder)
adblock_extension_path = 'Adblock Plus v3.11 (2).crx'  # Example path to .crx extension file

# Set up Chrome options to include the extension
chrome_options = Options()
chrome_options.add_extension(adblock_extension_path)


class MyTestClass(BaseCase):
    def test_jumia_with_adblock(self):
        # Set up the WebDriver with the specified options
        service = Service(executable_path='chromedriver/chromedriver')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the website
        self.open('https://www.kilimall.co.ke/')

        # # filling the form for the browser
        # fill_form = self.find_elements(By.NAME, 'email').send_keys('migelbrian3@gmail.com')
        # fill_form = self.find_elements(By.NAME, 'password').send_keys('')
        #
        # checkbox = self.find_elements(By.NAME, 'agree_terms')
        # if not checkbox.is_selected():
        #     checkbox.click()

        # submit form
        submit = self.find_elements(By.NAME, 'submit_button').click()

        # Perform actions on the page (same as before but using SeleniumBase methods)
        input_element = self.find_elements(By.CLASS_NAME, "van-field__body")

        # Wait for a while to see the results (SeleniumBase method)
        self.sleep(5)  # Using SeleniumBase sleep instead of time.sleep()

        # You can add further actions and assertions here as needed

        # Close the browser (SeleniumBase method)
        self.quit()

# To run the test, use pytest or the SeleniumBase CLI
