from models.employee_model import get_all_employees, add_employee, delete_employee
from models.department_model import get_all_departments, add_department
from models.certification_model import add_certification, get_certifications_by_employee
from models.payroll_model import add_payroll_record, get_payroll_records_by_employee
from models.leave_model import add_leave_record, get_leave_records_by_employee

def prompt_for_employee_details():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    birth_date = input("Birth Date (YYYY-MM-DD): ")
    gender = input("Gender: ")
    hire_date = input("Hire Date (YYYY-MM-DD): ")
    department_id = input("Department ID: ")
    address = input("Address: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    return (first_name, last_name, birth_date, gender, hire_date, department_id, address, phone_number, email)

def prompt_for_department_details():
    department_name = input("Department Name: ")
    job_title = input("Job Title: ")
    job_description = input("Job Description: ")
    location = input("Location: ")
    return (department_name, job_title, job_description, location)

def prompt_for_certification_details():
    employee_id = input("Employee ID: ")
    certification_name = input("Certification Name: ")
    issued_by = input("Issued By: ")
    issue_date = input("Issue Date (YYYY-MM-DD): ")
    expiration_date = input("Expiration Date (YYYY-MM-DD): ")
    return (employee_id, certification_name, issued_by, issue_date, expiration_date)

def prompt_for_payroll_details():
    employee_id = input("Employee ID: ")
    department_id = input("Department ID: ")
    base_salary = input("Base Salary: ")
    bonus = input("Bonus: ")
    payroll_date = input("Payroll Date (YYYY-MM-DD): ")
    gross_amount = input("Gross Amount: ")
    net_amount = input("Net Amount: ")
    deductions = input("Deductions: ")
    return (employee_id, department_id, base_salary, bonus, payroll_date, gross_amount, net_amount, deductions)

def prompt_for_leave_details():
    employee_id = input("Employee ID: ")
    leave_start_date = input("Leave Start Date (YYYY-MM-DD): ")
    leave_end_date = input("Leave End Date (YYYY-MM-DD): ")
    leave_reason = input("Leave Reason: ")
    approval_status = input("Approval Status: ")
    return (employee_id, leave_start_date, leave_end_date, leave_reason, approval_status)

def list_employees():
    employees = get_all_employees()
    for emp in employees:
        print(dict(emp))

def list_departments():
    departments = get_all_departments()
    for dept in departments:
        print(dict(dept))

def list_certifications(employee_id):
    certifications = get_certifications_by_employee(employee_id)
    for cert in certifications:
        print(dict(cert))

def list_payroll_records(employee_id):
    payrolls = get_payroll_records_by_employee(employee_id)
    for payroll in payrolls:
        print(dict(payroll))

def list_leave_records(employee_id):
    leaves = get_leave_records_by_employee(employee_id)
    for leave in leaves:
        print(dict(leave))
