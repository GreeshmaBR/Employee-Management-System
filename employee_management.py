import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Greeshmagowda@123",
    database="employee_db"
)

cursor = connection.cursor()

emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
department = input("Enter Department: ")
salary = float(input("Enter Salary: "))

query = """
INSERT INTO employees(emp_id, name, department, salary)
VALUES (%s, %s, %s, %s)
"""

values = (emp_id, name, department, salary)

cursor.execute(query, values)

connection.commit()

print("Employee added successfully!")

cursor.close()
connection.close()