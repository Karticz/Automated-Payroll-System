import sqlite3

# 1. Connect to a database file on your D drive
# If the file doesn't exist, Python will create it automatically
db_path = r'D:\Payroll_Project\company_data.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 2. Create the Employee table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        hourly_rate REAL,
        hours_worked REAL
    )
''')

# 3. Add some sample data (only run this once)
sample_staff = [
    (101, 'Alice Smith', 25.0, 160),
    (102, 'Bob Johnson', 20.0, 150),
    (103, 'Charlie Brown', 30.0, 140)
]
cursor.executemany('INSERT OR IGNORE INTO employees VALUES (?,?,?,?)', sample_staff)

conn.commit()
conn.close()
print("Database and table created successfully on D: Drive!")