from PageObjects.Add_Edit_Delete import PIMAutomation, Credentials
import pytest

# Global setup to initialize PIMAutomation instance
pim = PIMAutomation()

#Test login
def test_login():
    pim.login()
    assert pim.login() is None  #Assuming `login()` raises no exceptions and returns `None`
    print(f"SUCCESS: Logged in with {Credentials.USERNAME}")


#Test Adding an employee
def test_add_employee():
    pim.navigate_to_pim()
    assert pim.add_employee() is None  #Assuming `add_employee()` returns `None` on success
    print(f"SUCCESS: Employee {Credentials.FIRST_NAME} {Credentials.LAST_NAME} added.")


#Test Editing an employee
def test_edit_employee():
    pim.navigate_to_pim()
    assert pim.edit_employee() is None  #Assuming `edit_employee()` returns `None` on success
    print(f"SUCCESS: Employee edited to {Credentials.FIRST_NAME} {Credentials.MIDDLE_NAME} {Credentials.LAST_NAME}.")


#Test Deleting an employee
def test_delete_employee():
    pim.navigate_to_pim()
    assert pim.delete_employee() is None  #Assuming `delete_employee()` returns `None` on success
    print(f"SUCCESS: Employee {Credentials.FIRST_NAME} {Credentials.MIDDLE_NAME} {Credentials.LAST_NAME} deleted.")


@pytest.fixture(scope="module", autouse=True)
def cleanup():
    """Clean up after all tests."""
    yield
    pim.driver.quit()
    print("SUCCESS: Automation completed and browser closed.")
