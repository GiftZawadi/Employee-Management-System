from models import get_db_connection

def add_employee(first_name, last_name, birth_date, gender, hire_date, department_id, address, phone_number, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (first_name, last_name, birth_date, gender, hire_date, department_id, address, phone_number, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, birth_date, gender, hire_date, department_id, address, phone_number, email))
    conn.commit()
    conn.close()

def get_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

def delete_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE employee_id = ?', (employee_id,))
    conn.commit()
    conn.close()
