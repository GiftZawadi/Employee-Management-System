from models import get_db_connection

def add_leave_record(employee_id, leave_start_date, leave_end_date, leave_reason, approval_status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO leave_records (employee_id, leave_start_date, leave_end_date, leave_reason, approval_status)
        VALUES (?, ?, ?, ?, ?)
    ''', (employee_id, leave_start_date, leave_end_date, leave_reason, approval_status))
    conn.commit()
    conn.close()

def get_leave_records_by_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM leave_records WHERE employee_id = ?', (employee_id,))
    leaves = cursor.fetchall()
    conn.close()
    return leaves
