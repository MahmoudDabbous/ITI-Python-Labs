from Database import Database
from Models.Employee import Employee
from Models.Manager import Manager

def main():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'password',
        'database': 'employees'
    }

    db = Database(config)
    db.connect()
    db.create_employee_table()

    while True:
        print("\nEmployee Management System")
        print("Choose an action:")
        print("add - Add new employee")
        print("m - Add new manager")
        print("list - List all employees")
        print("q - Quit")

        choice = input("> ").lower()

        if choice == 'add':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = int(input("Age: "))
            department = input("Department: ")
            salary = float(input("Salary: "))

            employee = Employee(first_name, last_name, age, department, salary, db)
            print("Employee added successfully!")

        elif choice == 'm':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = int(input("Age: "))
            department = input("Department: ")
            salary = float(input("Salary: "))
            managed_department = input("Managed Department: ")

            manager = Manager(first_name, last_name, age, department, salary, managed_department, db)
            print("Manager added successfully!")

        elif choice == 'list':
            employee = Employee(None, None, None, None, None, db) 
            employee.list_employees()

        elif choice == 'q':
            break

        else:
            print("Invalid choice. Please try again.")

    db.close()

if __name__ == "__main__":
    main()
