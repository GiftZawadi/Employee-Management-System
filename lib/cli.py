from helpers import *


def show_main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Delete Employee")
        print("4. Update Employee")
        print("5. View Employee by ID") 
        print("6. Add Department")
        print("7. View Departments")
        print("8. Add Certification")
        print("9. View Certifications")
        print("10. Add Payroll Record")
        print("11. View Payroll Records")
        print("12. Add Leave Record")
        print("13. View Leave Records")
        print("14. Exit")
        choice = input("Choose an option (1-14): ") 

        if choice == '1':
            details = prompt_for_employee_details()
            add_employee(*details)
            print("Employee added successfully!")
        elif choice == '2':
            list_employees()
        elif choice == '3':
            employee_id = input("Enter Employee ID to delete: ")
            delete_employee(employee_id)
            print(f"Employee with ID {employee_id} deleted!")
        elif choice == '4':
            employee_id, first_name, last_name, birth_date, gender, hire_date, department_id, address, phone_number, email = prompt_for_employee_update()
            existing_employee = get_employee_by_id(employee_id)

            if existing_employee:
                update_employee(
                    employee_id,
                    first_name if first_name else existing_employee['first_name'],
                    last_name if last_name else existing_employee['last_name'],
                    birth_date if birth_date else existing_employee['birth_date'],
                    gender if gender else existing_employee['gender'],
                    hire_date if hire_date else existing_employee['hire_date'],
                    department_id if department_id else existing_employee['department_id'],
                    address if address else existing_employee['address'],
                    phone_number if phone_number else existing_employee['phone_number'],
                    email if email else existing_employee['email']
                )
                print(f"Employee with ID {employee_id} updated!")
            else:
                print(f"No employee found with ID {employee_id}.")
        elif choice == '5': 
            employee_id = input("Enter Employee ID to view: ")
            view_employee_by_id(employee_id)
        elif choice == '6':
            details = prompt_for_department_details()
            add_department(*details)
            print("Department added successfully!")
        elif choice == '7':
            list_departments()
        elif choice == '8':
            details = prompt_for_certification_details()
            add_certification(*details)
            print("Certification added successfully!")
        elif choice == '9':
            employee_id = input("Enter Employee ID to view certifications: ")
            list_certifications(employee_id)
        elif choice == '10':
            details = prompt_for_payroll_details()
            add_payroll_record(*details)
            print("Payroll record added successfully!")
        elif choice == '11':
            employee_id = input("Enter Employee ID to view payroll records: ")
            list_payroll_records(employee_id)
        elif choice == '12':
            details = prompt_for_leave_details()
            add_leave_record(*details)
            print("Leave record added successfully!")
        elif choice == '13':
            employee_id = input("Enter Employee ID to view leave records: ")
            list_leave_records(employee_id)
        elif choice == '14':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 14.")

if __name__ == '__main__':
    show_main_menu()
