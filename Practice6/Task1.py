#1.Create a class named Car that has the following attributes: make, model, and year. 
#It should also have a method called get_info() that returns a string with the car's make, model, and year.

class Car:
    def __init__(self,make,model,year) -> None:
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        return "Make: " + self.make + ", Model: " + self.model + ", Year: " + str(self.year)
    
car = Car("Audi","A3",1999)
car2 = Car("Volvo","D65",2007)
print(car.get_info())
print(car2.get_info())