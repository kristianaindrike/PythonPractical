#Create a class named Animal that has the following attributes: name and species. 
#It should also have a method called speak() that returns a string with the animal's sound.

from dataclasses import dataclass

@dataclass
class Animal:
    name:str
    species:str

    def speak(self):
        return "meow"
    
animal = Animal("Cat","Cats")

print(animal.speak())
  