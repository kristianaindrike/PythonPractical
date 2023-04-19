from dataclasses import dataclass

@dataclass
class Car:
    make:str
    model:str
    year:int

car1 = Car("Volvo","D65",2007)
car2 = Car("Nisan","New",2020)
print(car1)
print(car2)
