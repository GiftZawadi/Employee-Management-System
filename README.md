## Employee Management

This is a CLI and ORM project by Gift Zawadi first created in June 2024

## Description

Employee Management System is a command-line interface (CLI) application built in Python to help employers manage their employee departments and records. This application is built with Python and uses SQLite for data storage, offering a modular and scalable approach to handling employee-related data. It allows users to interact with and manipulate employee-related information conveniently from the terminal. The project demonstrates basic CRUD (Create, Read, Update, Delete) operations.

## Features

1. Employee Managment.
Add Employee- Allows you to add a new employee to the system.
View All Employees- Lists all employees in the system with their details.
Delete Employee- Deletes an employee from the system based on their unique ID.
Update Employee- Updates the details of an existing employee.
View Employee by ID- Retrieves and displays the details of an employee by their ID.
2. Department Management.
Add Department- Adds a new department to the system.
View All Departments- Lists all departments available in the system.
3. Certification Management.
Add Certification- Records a new certification for an employee.
View Certifications-  Lists all certifications for a specified employee.
4. Payroll Management.
Add Payroll Record- Adds a payroll record for an employee.
View Payroll Records- Lists all payroll records for a specified employee.
5. Leave Management.
Add Leave Record- Records a leave entry for an employee.
View Leave Records- Lists all leave records for a specified employee.
6. User Interface
Text-Based CLI: The application operates through a Command-Line Interface, providing text-based interaction.
Prompt-Driven Navigation: Users navigate through the application by selecting numbered options and entering required details as prompted.
7. Database Management
SQLite Integration: The application uses SQLite for data storage, ensuring data persistence across sessions.
Data Integrity: The system ensures the integrity of data through proper foreign key relationships and constraints.
8. Data Handling
Modular Code: The application is organized into various modules and helper functions to maintain code clarity and ease of maintenance.
Prompt-Based Input: Data is collected through user prompts, making the application interactive and user-friendly.
9. Error Handling and Validation
Error Messages: The application provides meaningful error messages for invalid inputs or operations, such as when trying to update or view a non-existent employee.
Input Validation: Ensures that data entered meets the expected format and requirements.

## Directory Structure
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── employee_model.py
    │   ├── department_model.py
    │   ├── certification_model.py
    │   ├── payroll_record_model.py
    │   └── leave_record_model.py
    ├── cli.py
    ├── debug.py
    └── helpers.py

## Installation Requirements

A computer with access to the internet. Bash terminal with pipenv installed.

## How to Run

Setup

Clone the repository and navigate to project directory:

`git@github.com:GiftZawadi/Employee-Management-System.git`

cd 

`Employee-Management-System`

Or by downloading a ZIP file of the code. The repository, if downloaded as a .zip file will need to be extracted to your preferred location.

Install the dependacies and launch shell environment

`pipenv install`

`pipenv shell`

Initialize the database

`python3 _init_.py`

## Usage

To run the apllication use

`python3 lib/cli.py`

Follow the on-screen instructions to register/login, manage pets, log health records, set appointments, and view information.

## CLI Menu Options

--- Employee Management System ---
1. Add Employee
2. View Employees
3. Delete Employee
4. Update Employee
5. View Employee by ID
6. Add Department
7. View Departments
8. Add Certification
9. View Certifications
10. Add Payroll Record
11. View Payroll Records
12. Add Leave Record
13. View Leave Records
14. Exit

## Acknowledgement


# Acknowledgements

This project is based on the template and curriculum provided by Flatiron School.

## Contributing

Contributions are welcome! If you find any issues or would like to suggest new features, please open an issue or create a pull request.

## Technologies used

Python.
Python libraries and modules.
SQL.
SQLite.

## Contact
For any questions or concerns please reach out to me at:
[github.com/GiftZawadi] or [gzomandi07@gmail.com]
 
## License

Copyright (c) 2024 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.














