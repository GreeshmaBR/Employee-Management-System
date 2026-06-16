import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Greeshmagowda@123",
    database="employee_db"
)

cursor = connection.cursor()

emp_id = int(input("Enter Employee ID to delete: "))

query = "DELETE FROM employees WHERE emp_id = %s"

cursor.execute(query, (emp_id,))

connection.commit()

print("Employee deleted successfully!")

cursor.close()
connection.close()