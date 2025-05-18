# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# Solution:
class Person():
    def __init__(self, name):
        self.name = name
        #print(f"Person created with name: {self.name}")
        
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        #print(f"Teacher created with subject: {self.subject}")
# Create an instance of Teacher
teacher = Teacher("Alice", "Mathematics")
# Access the name and subject
print(f"Teacher Name: {teacher.name}")
print(f"Teacher Subject: {teacher.subject}")






               