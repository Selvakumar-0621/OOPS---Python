from PageObjects.Add_Edit_Delete import PIMAutomation

#Global setup to initialize Homepage instance
pim = PIMAutomation()

#Test Logging in with valid Username and password
def test_login():
    assert pim.login() is None
    print("Success : Logged in successfully!")

#Test Navigating to PIM Module
def test_navigate_to_pim():
    assert pim.navigate_to_pim() is None
    print("Success : Navigated to PIM module.")

#Test Adding an employee in PIM
def test_add_employee():
    assert pim.add_employee() is None
    print("Success : Employee added successfully!")

#Test again navigating to PIM Module
def test_navigate_to_pim1():
    assert pim.navigate_to_pim1() is None
    print("Success : Again Navigated to PIM module.")

#Test Editing the added employee details and saving it
def test_edit_employee():
    assert pim.edit_employee() is None
    print("Success : Employee edited successfully!")

#Test again navigating to PIM Module
def test_navigate_to_pim2():
    assert pim.navigate_to_pim2() is None
    print("Success : Again Navigated to PIM module.")

#Test Deleting the Added and Edited Employee
def test_delete_employee():
    assert pim.delete_employee() is None
    print("Success : Employee deleted successfully!")

#Test Closing the browser
def test_shutdown():
    assert pim.shutdown() is None
    print("Success : Automation Shutting Down")
    print("SUCCESS: Automation completed and browser closed.")