# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


# Solution:
class Counter():
    count = 0 # class variable to keep track of object count
    def __init__(self):
        Counter.count += 1 # increment the count whenever a new object is created

    @classmethod
    def display_count(cls): # class method to display the count
        print(f"Number of objects created: {cls.count}")
        
        
c1 = Counter() # create first object
c2 = Counter() # create second object	
c3 = Counter() # create third object
Counter.display_count() # call the class method to display the count        
        