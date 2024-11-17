
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Credentials:
    # Login data
    USERNAME = "Admin"
    PASSWORD = "admin123"

    # Employee data
    FIRST_NAME = "Walter"
    LAST_NAME = "White"
    MIDDLE_NAME = "Heisenberg"


class Locators:
    # Login page locators
    USERNAME_BOX = "username"
    PASSWORD_BOX = "password"
    LOGIN_BUTTON = "//div[@class='oxd-form-actions orangehrm-login-action']/button"

    # PIM Module locators
    PIM_MODULE = "//span[text()='PIM']"
    ADD_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button[1]"
    FIRST_NAME_BOX = "firstName"
    LAST_NAME_BOX = "lastName"
    FEMALE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span"
    SAVE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"
    CONFIRM_SAVE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button"
    EDIT_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]"
    MIDDLE_NAME_BOX = "middleName"
    MALE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span"
    SAVE_EDIT_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button"
    EMPLOYEE_NAME_LOCATOR = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
    SEARCH_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
    DELETE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]"
    CONFIRM_DELETE_BUTTON = "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]"
    ID_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/label"

class PIMAutomation:
    URL = "https://opensource-demo.orangehrmlive.com/"

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def get_locator(self, locator):
        return (By.XPATH, locator) if "/" in locator else (By.NAME, locator)


#Method to login with login credentials
    def login(self):
        try:
            self.driver.find_element(By.NAME, Locators.USERNAME_BOX).send_keys(Credentials.USERNAME)
            self.driver.find_element(By.NAME, Locators.PASSWORD_BOX).send_keys(Credentials.PASSWORD)
            self.driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
            print("Logged in Successfully")
        except Exception as e:
            print(f"Failed to login: {e}")


#Method to navigate to PIM Module to perform expected actions
    def navigate_to_pim(self):
        try:
            pim_locator = self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.PIM_MODULE)))
            pim_locator.click()
            print("Navigated to PIM module.")
        except (TimeoutException, NoSuchElementException) as e:
            print(f"An error occurred while navigating to PIM: {e}")




#Method to add an employee with name as "Walter White" & Gender as "Female
    def add_employee(self):
        try:
            add_locator = self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.ADD_BUTTON)))
            add_locator.click()

            self.wait.until(EC.presence_of_element_located(self.get_locator(Locators.FIRST_NAME_BOX))).send_keys(Credentials.FIRST_NAME)
            self.wait.until(EC.presence_of_element_located(self.get_locator(Locators.LAST_NAME_BOX))).send_keys(Credentials.LAST_NAME)

            self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.SAVE_BUTTON))).click()

            self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.FEMALE_BUTTON))).click()
            print("Employee added successfully! Walter White - Female")

            self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.CONFIRM_SAVE_BUTTON))).click()
        except (TimeoutException, NoSuchElementException) as error:
            print("An error occurred while adding an employee:", error)




#Method to edit the created employee with name as " Walter Heisenberg White" & gender as "Male"
    def edit_employee(self):
        try:
            employee_locator = self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.EMPLOYEE_NAME_LOCATOR)))
            employee_locator.click()

            self.wait.until(EC.presence_of_element_located(self.get_locator(Locators.EMPLOYEE_NAME_LOCATOR))).send_keys(Credentials.FIRST_NAME)

            self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.SEARCH_BUTTON))).click()

            self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.ID_BUTTON))).click()

            edit_locator = self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.EDIT_BUTTON)))
            edit_locator.click()

            self.wait.until(EC.presence_of_element_located(self.get_locator(Locators.MIDDLE_NAME_BOX))).send_keys(Credentials.MIDDLE_NAME)
            self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.MALE_BUTTON))).click()
            self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.SAVE_EDIT_BUTTON))).click()

            print("Employee Edited Successfully", Credentials.FIRST_NAME, Credentials.MIDDLE_NAME, Credentials.LAST_NAME, " - Male")
            self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.CONFIRM_SAVE_BUTTON))).click()
        except (TimeoutException, NoSuchElementException) as error:
            print("An error occurred while adding an employee:", error)




#Method to delete the edited employee "Walter Heisenberg White"
    def delete_employee(self):
        try:
            employee_locator = self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.EMPLOYEE_NAME_LOCATOR)))
            employee_locator.click()

            self.wait.until(EC.presence_of_element_located(self.get_locator(Locators.EMPLOYEE_NAME_LOCATOR))).send_keys(Credentials.FIRST_NAME)

            self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.ID_BUTTON))).click()

            self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.SEARCH_BUTTON))).click()

            delete_locator = self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.DELETE_BUTTON)))
            delete_locator.click()

            confirm_delete_locator = self.wait.until(EC.element_to_be_clickable(self.get_locator(Locators.CONFIRM_DELETE_BUTTON)))
            confirm_delete_locator.click()

            print("Employee Deleted Successfully - Walter Heisenberg White - Male")


        except (TimeoutException, NoSuchElementException) as error:
            print("An error occurred while adding an employee:", error)

        finally:
            self.driver.quit()



#Main Function Execution

if __name__ == "__main__":
    pim_automation = PIMAutomation()
    pim_automation.login()
    pim_automation.navigate_to_pim()
    pim_automation.add_employee()
    pim_automation.navigate_to_pim()
    pim_automation.edit_employee()
    pim_automation.navigate_to_pim()
    pim_automation.delete_employee()
    pim_automation.driver.quit()


"""
While executing the program if already the employee exists then only the error is occurring
Now I had made the changes that resulted the excepted output and
I have attached the text file with screenshots of output from the console for your reference.
"""