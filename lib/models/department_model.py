from models import get_db_connection

def add_department(department_name, job_title, job_description, location):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO job_departments (department_name, job_title, job_description, location)
        VALUES (?, ?, ?, ?)
    ''', (department_name, job_title, job_description, location))
    conn.commit()
    conn.close()

def get_all_departments():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM job_departments')
    departments = cursor.fetchall()
    conn.close()
    return departments
