AT Project 1

Test Case ID: TC_Login_01

Test Case Description: Verify a user can successfully log in to the website using a valid username and password.

Steps:
1.	Launch the URL in a compatible web browser.
2.	Enter a valid username in the username field.
3.	Enter the corresponding valid password for the username in the password field.
4.	Click the "Login" button.

Expected Result:
1.	The website redirects the user to the expected landing page after successful login.
2.	The landing page should be in the Dashboard Module present on the left side by default
3.	This verifies that the login is being done successful.

Pass/Fail Criteria:
●	Pass: The user is successfully logged in and redirected to the expected landing page with Dashboard module being selected.

●	Fail: The user is not logged in, or an error message is displayed indicating “Invalid credentials”.

This ensures the basic login functionality works as expected with valid credentials.

Actual Result:
1.	The website redirects the user to the expected landing page after successful login.
2.	The landing page is in the Dashboard Module present on the left side by default.
3.	This verifies that the login is done successful.





Test Case ID: TC_Login_02

Test Case Description: Verify a user can log in to the website using a valid username and Invalid password.

Steps:
1. Launch the URL in a compatible web browser.
2. Enter a valid username in the username field.
3. Enter the Invalid password for the password in the password field.
4.	Click the "Login" button.

Expected Result:
1. The website remains the user in the same login page stating Invalid credentials.
2. This verifies that the login is being unsuccessful due to invalid credentials

Pass/Fail Criteria:
●	Pass: The user is not logged in, or an error message is displayed indicating “Invalid credentials”.
●	Fail: The user is successfully logged in and redirected to the expected landing page with Dashboard module being selected with Invalid Credentials.

This positive test case ensures the basic login functionality works as expected with Invalid credentials.

Actual Result:
1.	The website remains in the same Login page.
2.	The website shows error message stating Invalid Credentials.

 







Test Cases Dealing With PIM
Test Case ID: TC_PIM_01

Test Case Description:  To add a New Employee in the PIM Module

Steps:
1.	Launch the URL in a compatible web browser.
2.	Enter a valid username in the username field.
3.	Enter the corresponding valid password for the username in the password field.
4.	Click the "Login" button.
5.	Click the “PIM” module present on the left side of the Home page.
6.	Click Add button
7.	Enter the First name, Last name of the employee.
8.	Click save button.
9.	Select Female Checkbox in the personal details tab.
10.	Click save button



Expected Result:
1.	The Login Page should be displayed after launching the URL.
2.	After entering valid username and password the website should go to the landing page with Dashboard Module present on the left side by default.
3.	After clicking PIM Module, the website should move to the Employee information tab.
4.	After clicking Add button, the webpage should direct to Add Employee tab.
5.	After clicking Save button, the webpage should direct to Personal details tab.
6.	After selecting Gender and clicking save, the webpage saves the data and remains in the same page.

This ensures the basic login functionality works as expected by adding a New Employee to the PIM Module


Actual Result:
1.	The website goes to the landing page with Dashboard Module present on the left side by default after logging in with valid Username and Password.
2.	After Clicking PIM Module, the webpage directs to the Employee Information Tab.
3.	After Clicking Add button, the web page directs to the Add Employee Tab.
4.	After entering Employee name, and clicking save button, the web page directs to the Employee’s Personal details tab.
5.	After Entering the employee personal details and clicking save button the webpage displays the toast message as Success.
 
 This ensures the functionality of Adding an Employee to the PIM Module.






Test Case ID: TC_PIM_02

Test Case Description:  To edit the added Employee in the PIM Module

Steps:
1.	Click the PIM Module
2.	Enter the first name of the added employee in the employee’s name box and click search button.
3.	Select the employee’s name from the bottom and click edit button.
4.	Add the middle name and change the Gender and click save button

   
Actual Result:
1.	After entering the first name in the Employee’s name field and click search, the added employee was listed below.
2.	After clicking the Edit button the web page directed to the employee personal detail tab
3.	After editing the personal info of the employee and clicking save button toast message displayed as “Successfully Updated”.


This ensures the basic login functionality works as expected by adding a New Employee to the PIM Module


Actual Result:
1.	The website goes to the landing page with Dashboard Module present on the left side by default after logging in with valid Username and Password.
 
This ensures the functionality of Editing the added Employee details in the PIM Module.





Test Case ID: TC_PIM_03

Test Case Description:  To delete the added Employee in the PIM Module

Steps:
1.	Click the PIM Module
2.	Enter the first name of the added employee in the employee’s name box and click search button.
3.	Select the employee’s name from the bottom and click delete button.
4.	Click on the “Ok Delete” button.


Actual Result:
•	After entering the employee first name and clicking search button the employee name is displayed below.
•	After clicking on the Delete button the confirmation box is displayed.
•	After clicking on the “Yes, Delete” button the employee and the employee’s data is deleted from the PIM Module.


This ensures the functionality of Deleting the Employee and the employee’s details in the PIM Module.

