# Importing necessary libraries and modules
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import Data
from Test_Locator.Locator import Locators
from selenium.webdriver.firefox.service import service, Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

# Defining a test class named Test_Raja
class Test_Raja:
    # Fixture to set up and tear down the test environment
    @pytest.fixture(autouse=True)
    def setup(self):
        # Initialize test-specific variables and resources
        self.locator = Locators()
        # Initialize a Firefox web driver using GeckoDriverManager
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield # This allows the test to run
        # Close the web driver at the end of the test
        self.driver.close()

    # A function to check the visibility of an element
    def is_element_visible(self, by, value):
        try:
            element = self.driver.find_element(by=by, value=value)
            print(f'{element.text} is displayed')
            return element.is_displayed()
        except Exception:
            return False

    # Test function to check the Header page
    def test_check_header_page(self):
        # Navigate to the URL defined in Data_1
        self.driver.get(Data.Data_1().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located)

        # Fill in username and password input fields and click the submit button

        self.driver.find_element(by=By.NAME, value=self.locator.username_input_box).send_keys(Data.Data_1().username)
        self.driver.find_element(by=By.NAME, value=self.locator.password_input_box).send_keys(Data.Data_1().password)
        self.driver.find_element(by=By.XPATH, value=self.locator.submit_button).click()
        sleep(3)

        # Click on the admin element and check the visibility of Menu items
        self.driver.find_element(by=By.XPATH, value=self.locator.admin_xpath).click()
        assert self.is_element_visible(By.XPATH, self.locator.usermanagement_xpath)
        assert self.is_element_visible(By.XPATH, self.locator.job_xpath)
        assert self.is_element_visible(By.XPATH, self.locator.organization_xpath)
        sleep(2)
        assert self.is_element_visible(By.XPATH, self.locator.qualifications_xpath)
        assert self.is_element_visible(By.XPATH, self.locator.nationalities_xpath)
        assert self.is_element_visible(By.XPATH, self.locator.branding_xpath)
        assert self.is_element_visible(By.XPATH, self.locator.config_xpath)


