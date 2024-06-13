from helpers import *

def show_main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Delete Employee")
        print("4. Add Department")
        print("5. View Departments")
        print("6. Add Certification")
        print("7. View Certifications")
        print("8. Add Payroll Record")
        print("9. View Payroll Records")
        print("10. Add Leave Record")
        print("11. View Leave Records")
        print("12. Exit")
        choice = input("Choose an option (1-12): ")

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
            details = prompt_for_department_details()
            add_department(*details)
            print("Department added successfully!")
        elif choice == '5':
            list_departments()
        elif choice == '6':
            details = prompt_for_certification_details()
            add_certification(*details)
            print("Certification added successfully!")
        elif choice == '7':
            employee_id = input("Enter Employee ID to view certifications: ")
            list_certifications(employee_id)
        elif choice == '8':
            details = prompt_for_payroll_details()
            add_payroll_record(*details)
            print("Payroll record added successfully!")
        elif choice == '9':
            employee_id = input("Enter Employee ID to view payroll records: ")
            list_payroll_records(employee_id)
        elif choice == '10':
            details = prompt_for_leave_details()
            add_leave_record(*details)
            print("Leave record added successfully!")
        elif choice == '11':
            employee_id = input("Enter Employee ID to view leave records: ")
            list_leave_records(employee_id)
        elif choice == '12':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 12.")

if __name__ == '__main__':
    show_main_menu()
