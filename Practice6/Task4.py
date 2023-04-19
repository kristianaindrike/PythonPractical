#Create a class named Person that has the following attributes: name, age, and address. 
#It should also have a method called get_info() that returns a string with the person's name, age, and address.

from dataclasses import dataclass

@dataclass
class Address:
    streat:str
    city:str
    country:str
    house_number:int


@dataclass
class Person:
    name:str
    age:int
    address:Address

    def get_info(self):
        return "Name: " + self.name + "Age: " + str(self.age) + "Address: " + self.address
    
address = Address("Elijas iela","Riga","Latvija",14)
person = Person("Kristiana",26,address)

print(person)
  