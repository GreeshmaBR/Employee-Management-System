import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Greeshmagowda@123",
    database="employee_db"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM employees")

employees = cursor.fetchall()

print("\nEmployee Records")
print("-" * 50)

for employee in employees:
    print(employee)

cursor.close()
connection.close()