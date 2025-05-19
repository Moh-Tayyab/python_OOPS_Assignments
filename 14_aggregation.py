# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# Solution:
class Employee():
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f"Employee Name: {self.name}")    
        
        
class Department():
    def __init__(self, name):
        self.name = name
        self.employee = []
        
    def add_employee(self, employee):
        self.employee.append(employee)
        print(f"Added {employee.name} to {self.name} department")
        
    def show_employees(self):
        print(f"Employees in {self.name} department:")
        for emp in self.employee:
            emp.display()
               
        
e1 = Employee("Alice")
e2 = Employee("Bob")
dept = Department("HR")
dept.add_employee(e1)
dept.add_employee(e2)
dept.show_employees()
        