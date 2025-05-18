# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

# Solution:
class Bank():
    bank_name = "Meezan Bank" # class variable to keep track of bank name
    
    @classmethod
    def change_bank_name(cls, name): # class method to change the bank name
        cls.bank_name = name
        print(f"Bank name changed to {cls.bank_name}")   

# create an object of Bank class
b = Bank()
print(b.bank_name) # access the class variable
b.change_bank_name("Al Baraka Bank") # change the bank name using class method    