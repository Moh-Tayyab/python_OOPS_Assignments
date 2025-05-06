# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

# Solution:
class student():
    # constructor
    def __init__(self, name, marks):
        self.name = name # instance variable / attribute
        self.marks = marks
        
    def display(self): # instance method
        print(f"Name: {self.name}, Marks: {self.marks}") 
       
s1 = student("John", 85) # create an object of the class
s1.display()    # call the method to display student details        
