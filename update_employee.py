import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Greeshmagowda@123",
    database="employee_db"
)

cursor = connection.cursor()

emp_id = int(input("Enter Employee ID to update: "))
new_salary = float(input("Enter new salary: "))

query = """
UPDATE employees
SET salary = %s
WHERE emp_id = %s
"""

cursor.execute(query, (new_salary, emp_id))

connection.commit()

print("Employee salary updated successfully!")

cursor.close()
connection.close()