from Database import Database

class Employee:
    employee_list = []

    def __init__(self, first_name, last_name, age, department, salary, db):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        self.db = db
        Employee.employee_list.append(self)
        sql = "INSERT INTO employee (first_name, last_name, age, department, salary) VALUES (%s, %s, %s, %s, %s)"  # Use %s for placeholders
        db.cursor.execute(sql, (first_name, last_name, age, department, salary))
        db.conn.commit()


    def transfer(self, new_department):
        self.department = new_department
        self.db.cursor.execute("UPDATE employee SET department = ? WHERE first_name = ? AND last_name = ?", (new_department, self.first_name, self.last_name))
        self.db.conn.commit()

    def list_employees(self):
      self.db.cursor.execute("SELECT * FROM employee")
      for row in self.db.cursor.fetchall():
        print(f"Name: {row[0]} {row[1]}, Age: {row[2]}, Department: {row[3]}, Salary: {row[4]}")

    def show(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}")

