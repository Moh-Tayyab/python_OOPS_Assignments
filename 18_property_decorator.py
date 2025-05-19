# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product():
    def __init__(self, price):
        self.__price = price
        
    @property    
    def price(self):
        return f"price {self.__price}"
        
    @price.setter
    def price(self, value):
        if value < 0:
            print("price cannot be negative!")  
        else:
            print("setting price..")
            self.__price = value
            
    @price.deleter
    def price(self):
        print("deleting price..")
        del self.__price     
        

p = Product(1000) 

print(p.price)         # ✅ price 1000
p.price = 1200         # ✅ setting price
print(p.price)         # ✅ price 1200

p.price = -600         # ❌ price cannot be negative!

del p.price            # ✅ deleting price


          