import pytest
from PageObjects.Homepage import Homepage
from PageObjects.Homepage import Data

#Global setup to initialize Homepage instance
homepage = Homepage()

self = homepage.driver.get("https://opensource-demo.orangehrmlive.com/")


#Test login
def test_start():
    homepage.start()
    assert homepage.start() is None
    print("Success : Automation Started")


#Test Username box
def test_validate_username():
    homepage.validate_username()
    assert homepage.validate_username() == True
    print("Success : Username Input Box is displayed")


#Test Password box
def test_validate_password():
    homepage.validate_password()
    assert homepage.validate_password() == True
    print("Success : Password Input Box is displayed")


#Test Submit Button
def test_validate_submit_button():
    homepage.validate_submit_button()
    assert homepage.validate_submit_button() == True
    print("Success : Login Button is enabled")



def test_login_1():
    homepage.login_1()
    assert homepage.login_1() == False
    print("Invalid Credentials : with {a} and {b} ".format(a=Data().username_1, b=Data().password_1))



def test_login():
    homepage.login()
    assert homepage.login() == False
    print("Success : Login with {a} and {b} ".format(a=Data().username, b=Data().password))



def test_shutdown():
    homepage.shutdown()
    assert homepage.shutdown() is None
    print("Success : Automation Shutting Down")



@pytest.fixture(scope="module", autouse=True)
def cleanup():
    """Clean up after all tests."""
    yield
    homepage.driver.quit()
    print("SUCCESS: Automation completed and browser closed.")