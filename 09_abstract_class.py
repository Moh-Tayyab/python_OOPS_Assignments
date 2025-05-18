# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

# Solution:
from abc import ABC, abstractmethod

class Shape():
    @abstractmethod
    def area(self):
        pass  # Abstract
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
rect = Rectangle(5, 10)
print(f"Area of rectangle: {rect.area()}")    

    