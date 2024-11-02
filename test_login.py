
from PageObjects.Homepage import Data
from PageObjects.Homepage import Homepage
from PageObjects.Add_Edit_Delete import PIMAutomation as pim

def test_start():
    assert Homepage().start() == True
    print("Success : Automation Started")


def validate_username(self):
    assert Homepage().validate_username() == True
    print("Success : Username Input Box is displayed")


def validate_password(self):
    assert Homepage().validate_password() == True
    print("Success : Password Input Box is displayed")


def validate_submit_button(self):
    assert Homepage().validate_submit_button() == True
    print("Success : Login Button is enabled")


def login(self):
    assert Homepage().login() == True
    print("Success : Login with {a} abd {b} ".format(a=Data().username, b=Data().password))


def login_1(self):
    assert Homepage().login_1() == False
    print("Success : Login with {a} abd {b} ".format(a=Data().username_1, b=Data().password_1))


def shutdown(self):
    assert Homepage().shutdown() is None
    print("Success : Automation Shutting Down")


def login(self):
    assert pim.login() == True
    print("Success : Login with {a} abd {b} ".format(a=Data().username, b=Data().password))

def navigate_to_pim(self):
    assert pim.navigate_to_pim() == True
    print("Success : Navigated to PIM module.")

def add_employee(self):
    assert pim.add_employee() == True
    print("Success : Employee added successfully!")

def navigate_to_pim(self):
    assert pim.navigate_to_pim() == True
    print("Success : Again Navigated to PIM module.")

def edit_employee(self):
    assert pim.edit_employee() == True
    print("Success : Employee edited successfully!")

def navigate_to_pim(self):
    assert pim.navigate_to_pim() == True
    print("Success : Again Navigated to PIM module.")

def delete_employee(self):
    assert pim.delete_employee() == True
    print("Success : Employee deleted successfully!")

def test_end():
    assert Homepage().shutdown() is None
    print("Success : Automation Ended")