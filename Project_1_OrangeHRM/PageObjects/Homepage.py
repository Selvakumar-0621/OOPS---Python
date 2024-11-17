from attr.setters import validate
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Data:
    url = "https://opensource-demo.orangehrmlive.com/"
    username = "Admin"
    password = "admin123"
    username_1 = "Admin"
    password_1 = "invalidpassword"


class Locators:
    username_box = "username"
    password_box = "password"
    login_button = "//div[@class='oxd-form-actions orangehrm-login-action']/button"


class Homepage(Data, Locators):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def start(self):
        self.driver.get(self.url)

    def validate_username(self):
        try:
            username = self.wait.until(EC.presence_of_element_located((By.NAME, self.username_box)))
            print("The Username Input Box is displayed")
            return True
        except:
            print("The Username Input Box is not displayed")
            return False

    def validate_password(self):

        try:
            password = self.wait.until(EC.presence_of_element_located((By.NAME, self.password_box)))
            print("The Password Input Box is displayed")
            return True
        except:
            print("The Password Input Box is not displayed")
            return False

    def validate_submit_button(self):

        try:
            login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, self.login_button)))
            if login_button.is_displayed():
                print("The Login Button is enabled")
                return True
        except:
            print("The Login Button is not enabled")
            return False

    def login_1(self):
        try:
            self.driver.find_element(By.NAME, self.username_box).send_keys(self.username_1)
            self.driver.find_element(By.NAME, self.password_box).send_keys(self.password_1)
            self.driver.find_element(By.XPATH, self.login_button).click()
            print("Failed to Login : Invalid Credentials")
            return False
        except:
            return None

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

    def shutdown(self):
        self.driver.quit()
        return None


if __name__ == "__main__":
    homepage = Homepage()
    homepage.start()
    homepage.validate_username()
    homepage.validate_password()
    homepage.validate_submit_button()
    homepage.login_1()
    homepage.login()
    homepage.shutdown()
