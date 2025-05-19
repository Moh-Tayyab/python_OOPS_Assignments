# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

# Solution:

class TemperatureConvertor():
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    

temp_in_celsius = 25
temp_in_fahrenheit = TemperatureConvertor.celsius_to_fahrenheit(temp_in_celsius)
print(f"{temp_in_celsius}°C is {temp_in_fahrenheit}°F") 