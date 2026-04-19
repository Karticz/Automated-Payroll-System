import sqlite3
import pandas as pd # Make sure you have installed this (pip install pandas openpyxl)
from datetime import datetime

def run_payroll():
    # Define paths
    db_path = r'D:\Payroll_Project\company_data.db'
    
    # 1. Fetch data from SQL
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM employees", conn)
    conn.close()

    # 2. Calculate Payroll Logic
    # Let's assume a 10% tax deduction
    df['Gross Pay'] = df['hourly_rate'] * df['hours_worked']
    df['Tax'] = df['Gross Pay'] * 0.10
    df['Net Pay'] = df['Gross Pay'] - df['Tax']

    # 3. Create a unique filename using today's date
    today = datetime.now().strftime('%Y-%m-%d')
    excel_file = f'D:\\Payroll_Project\\Reports\\Payroll_Report_{today}.xlsx'

    # 4. Save to Excel
    df.to_excel(excel_file, index=False)
    
    print(f"Success! Payroll report saved to: {excel_file}")

# Run the function
if _name_ == "_main_":
    run_payroll()