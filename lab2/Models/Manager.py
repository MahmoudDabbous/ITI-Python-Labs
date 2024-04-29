from .Employee import Employee

class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department,db):
        super().__init__(first_name, last_name, age, department, salary, db)
        self.managed_department = managed_department

    def show(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}, Managed Department: {self.managed_department}")

