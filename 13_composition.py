# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

# Solution:
class Engine:
   def start(self):
       print("Engine started")

class Car():
    def __init__(self, engine):
        self.engine = engine
    def start(self):
        print("Car is starting...")
        self.engine.start()           
  
  
my_engine = Engine()
my_car = Car(my_engine)
my_car.start()    