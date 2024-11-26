from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Data class to store application-specific data such as URLs and credentials.
class Data:
    url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    username_1 = "Admin"
    password_1 = "invalidpassword"


# Locators class to store element locators for the application.
class Locators:
    username_box = "username"
    password_box = "password"
    login_button = "//div[@class='oxd-form-actions orangehrm-login-action']/button"


# Homepage class to define methods for interacting with the login page.
class Homepage(Data, Locators):

    def __init__(self):
        # Initialize the Chrome WebDriver.
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.driver.maximize_window()             # Maximize the browser window.
        self.driver.get(self.url)                 # Open the specified URL.
        self.driver.implicitly_wait(10)            # Set implicit wait for WebDriver.
        self.wait = WebDriverWait(self.driver, 10) # Set explicit wait for WebDriver.

    def start(self):
        self.driver.get(self.url)                 #Navigate to the login page URL


#To Check if the username input box is present on the page
    def validate_username(self):
        try:
            username = self.wait.until(EC.presence_of_element_located((By.NAME, self.username_box)))
            print("The Username Input Box is displayed")
            return True
        except:
            print("The Username Input Box is not displayed")
            return False

#To Check if the password input box is present on the page
    def validate_password(self):

        try:
            password = self.wait.until(EC.presence_of_element_located((By.NAME, self.password_box)))
            print("The Password Input Box is displayed")
            return True
        except:
            print("The Password Input Box is not displayed")
            return False

#To Check if the login button is enabled and visible on the page
    def validate_submit_button(self):

        try:
            login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, self.login_button)))
            if login_button.is_displayed():
                print("The Login Button is enabled")
                return True
        except:
            print("The Login Button is not enabled")
            return False

#Attempt to log in with invalid credentials
    def login_1(self):
        try:
            self.driver.find_element(By.NAME, self.username_box).send_keys(self.username_1)
            self.driver.find_element(By.NAME, self.password_box).send_keys(self.password_1)
            self.driver.find_element(By.XPATH, self.login_button).click()
            print("Failed to Login : Invalid Credentials")
            return False
        except:
            return None

#Attempt to log in with valid credentials
    def login(self):

        try:
            self.driver.find_element(By.NAME, self.username_box).send_keys(self.username)
            self.driver.find_element(By.NAME, self.password_box).send_keys(self.password)
            self.driver.find_element(By.XPATH, self.login_button).click()
            print("Logged in Successfully")
            return True
        except:
            print("Failed to Login")
            return False

#Attempt to close browser
    def shutdown(self):
        self.driver.quit()
        return None



#pytest --html=Reports/report.html