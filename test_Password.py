# Importing necessary libraries and modules
from selenium import webdriver  # Import the Selenium webdriver
from selenium.webdriver.firefox.service import service, Service  # Import the Firefox service and Service modules
from selenium.webdriver.support.wait import WebDriverWait  # Import the WebDriverWait module
from Test_Data import Data  # Import the Data module from Test_Data
from Test_Locator import Locator  # Import the Locator module from Test_Locator
from webdriver_manager.firefox import GeckoDriverManager  # Import GeckoDriverManager from webdriver_manager
from selenium.webdriver.common.by import By  # Import the By module from selenium.webdriver.common.by
from time import sleep  # Import the sleep function from the time module
import pytest  # Import the pytest module


class Test_Raja:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))  # Set up Firefox webdriver
        yield
        self.driver.close()

    sleep(3)  # Introduce a sleep before the test method (consider moving it inside the method)

    def test_Password(self, setup):
        try:
            self.driver.maximize_window()  # Maximize the browser window
            self.driver.get(Data.Data_1().url)  # Open the specified URL
            self.driver.implicitly_wait(10)  # Set implicit wait time

            sleep(3)  # Introduce sleep for better synchronization
            # Click on the password reset label and enter the username and click reset button
            self.driver.find_element(by=By.XPATH, value=Locator.Locators().password_reset_label).click()
            self.driver.find_element(by=By.NAME, value=Locator.Locators().username_input_box).send_keys(Data.Data_1().username)
            self.driver.find_element(by=By.XPATH, value=Locator.Locators().reset_button).click()
            sleep(3)  # Introduce sleep for better synchronization
            print('Reset Password link Sent successfully')

        except Exception as e:
            print('Employee Can not able to reset Password Successfully')  # Print an error message if password reset fails
