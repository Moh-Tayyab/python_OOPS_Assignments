# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

# Solution:
class MathUtils:
	@staticmethod
	def add(a, b):  # static method to add two numbers
		return a + b

result = MathUtils.add(5, 10)  # call the static method
print(f"The sum is: {result}") 
