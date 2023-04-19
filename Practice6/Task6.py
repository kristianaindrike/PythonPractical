#.Create a base class named Vehicle that has the following attributes: make, model, and year. 
# It should also have a method called get_info() that returns a string with the vehicle's make, model, and year. 
# Then create two subclasses, Car and Truck, that inherit from Vehicle and add additional attributes and methods 
# specific to each type of vehicle.

from dataclasses import dataclass

@dataclass
class Vehicle:
    make:str
    model:str
    year:int

    def get_info(self):
        return "Make: " + self.make + ", Model: " + self.model + ", Year: " + str(self.year)

@dataclass  
class Car(Vehicle):
    color:str
    pass

@dataclass
class Truck(Vehicle):
    width:float
    pass

car1 = Vehicle("Volvo", "A3", 1999)
car2 = Car("Audi", "Premium", 2000,"Black")
car3 = Truck("Nissan", "A45G", 2020,4)

print(car1)
print(car2)
print(car3)
    
