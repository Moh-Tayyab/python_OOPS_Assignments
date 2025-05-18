# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

# Solution:
class Employee():
    def __init__(self, name, salary, ssn):
        self.name = name # public variable
        self._salary = salary # protected variable
        self.__ssn = ssn # private variable
        # print(f"Employee {self.name} created with salary {self._salary} and SSN {self.__ssn}")
        
        
e = Employee("John Doe", 50000, "123-45-6789")  
print(f"Employee Name: {e.name}")  # Accessing public variable
try:
	print(f"Employee Salary: {e._salary}")  # Accessing protected variable
except AttributeError as e:
    	print(f"Error accessing protected variable: {e}")      