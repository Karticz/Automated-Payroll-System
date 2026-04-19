import sqlite3


db_path = r'D:\Payroll_Project\company_data.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 2. Creating the Employee table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        hourly_rate REAL,
        hours_worked REAL
    )
''')

# 3. Adding some sample data 
sample_staff = [
    (101, 'Raj', 25.0, 160),
    (102, 'Johnson', 20.0, 150),
    (103, 'Kranthi', 30.0, 140)
]
cursor.executemany('INSERT OR IGNORE INTO employees VALUES (?,?,?,?)', sample_staff)

conn.commit()
conn.close()
print("Database and table created successfully on D: Drive!")
