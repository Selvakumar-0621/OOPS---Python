
from PageObjects.Homepage import Homepage
from PageObjects.Homepage import Data
from PageObjects.Homepage import Homepage as homepage

homepage = Homepage()




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
