from dataclasses import dataclass

@dataclass
class Rectangle:
    width:float
    height:float

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
rectangle1 = Rectangle(12,3)
rectangle2 = Rectangle(9,5)

print(rectangle1.area())
print(rectangle1.perimeter())

print(rectangle2.area())
print(rectangle2.perimeter())