from models import get_db_connection

def add_certification(employee_id, certification_name, issued_by, issue_date, expiration_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO certifications (employee_id, certification_name, issued_by, issue_date, expiration_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (employee_id, certification_name, issued_by, issue_date, expiration_date))
    conn.commit()
    conn.close()

def get_certifications_by_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM certifications WHERE employee_id = ?', (employee_id,))
    certifications = cursor.fetchall()
    conn.close()
    return certifications
