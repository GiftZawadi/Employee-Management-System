from models import get_db_connection

def add_payroll_record(employee_id, department_id, base_salary, bonus, payroll_date, gross_amount, net_amount, deductions):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO payroll_records (employee_id, department_id, base_salary, bonus, payroll_date, gross_amount, net_amount, deductions)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (employee_id, department_id, base_salary, bonus, payroll_date, gross_amount, net_amount, deductions))
    conn.commit()
    conn.close()

def get_payroll_records_by_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM payroll_records WHERE employee_id = ?', (employee_id,))
    payrolls = cursor.fetchall()
    conn.close()
    return payrolls
