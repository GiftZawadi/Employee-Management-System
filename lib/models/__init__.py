import sqlite3

DATABASE_PATH = 'employee_management.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            birth_date DATE,
            gender TEXT,
            hire_date DATE,
            department_id INTEGER,
            address TEXT,
            phone_number TEXT,
            email TEXT
        );

        CREATE TABLE IF NOT EXISTS job_departments (
            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_name TEXT NOT NULL,
            job_title TEXT,
            job_description TEXT,
            location TEXT
        );

        CREATE TABLE IF NOT EXISTS certifications (
            certification_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            certification_name TEXT,
            issued_by TEXT,
            issue_date DATE,
            expiration_date DATE,
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        );

        CREATE TABLE IF NOT EXISTS payroll_records (
            payroll_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            department_id INTEGER,
            base_salary REAL,
            bonus REAL,
            payroll_date DATE,
            gross_amount REAL,
            net_amount REAL,
            deductions REAL,
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
            FOREIGN KEY (department_id) REFERENCES job_departments(department_id)
        );

        CREATE TABLE IF NOT EXISTS leave_records (
            leave_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER,
            leave_start_date DATE,
            leave_end_date DATE,
            leave_reason TEXT,
            approval_status TEXT,
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        );
    ''')

    conn.commit()
    conn.close()

initialize_database()
