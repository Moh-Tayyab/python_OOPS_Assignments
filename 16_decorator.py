# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

# Solution:

def log_function_call(func):
    def wrapper():
        print("function is being call")
        func()
        #print("after function")
    return wrapper    

@log_function_call
def say_hello():
    print("Hello, World!")
    
say_hello()    