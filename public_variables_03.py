# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

# Solution:

class Car():
    def __init__(self, brand):
        self.brand = brand #public variable
        
    def start(self): # public method
        print(f"{self.brand} is my farvorite car!")
        
        
c = Car("Mercedes") # create an object of Car class
print(c.brand) # access the public variable 
c.start() # call the public method
            