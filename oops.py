#single inheritance
#a child class inherits from a single parent class
class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def drive(self):
        print("car is driving")
car =Car()
car.start()
car.drive()


#multiple inheritance
#a child class inherits from multiple parent classes
class Engine:
    def engine_type(self):
        print("this vehicle has a disesel engine")
class Wheels:
    def number_of_wheels(self):
        print("this vehicle has four wheels")
class Truck(Engine,Wheels):
    pass
truck=Truck()
truck.engine_type()
truck.number_of_wheels()