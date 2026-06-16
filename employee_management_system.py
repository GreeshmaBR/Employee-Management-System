import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Greeshmagowda@123",
    database="employee_db"
)

cursor = connection.cursor()

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee Salary")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        query = """
        INSERT INTO employees(emp_id, name, department, salary)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (emp_id, name, department, salary))
        connection.commit()

        print("Employee added successfully!")

    elif choice == "2":
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        print("\nEmployee Records")
        print("-" * 50)

        for employee in employees:
            print(employee)

    elif choice == "3":
        emp_id = int(input("Enter Employee ID: "))
        salary = float(input("Enter New Salary: "))

        query = """
        UPDATE employees
        SET salary = %s
        WHERE emp_id = %s
        """

        cursor.execute(query, (salary, emp_id))
        connection.commit()

        print("Salary updated successfully!")

    elif choice == "4":
        emp_id = int(input("Enter Employee ID to delete: "))

        query = "DELETE FROM employees WHERE emp_id = %s"

        cursor.execute(query, (emp_id,))
        connection.commit()

        print("Employee deleted successfully!")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")

cursor.close()
connection.close()