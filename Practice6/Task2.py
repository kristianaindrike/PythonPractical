#2.Create a class named Rectangle that has the following attributes: width and height. 
#It should also have methods called area() and perimeter() that return the area and perimeter of the rectangle, 
#respectively.

class Rectangle:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height

    def area(self):
        return "Area: " + str((self.width * self.height)) 
    def perimeter(self):
        return ", Perimeter: " + str(2*(self.width + self.height))
    
measure1 = Rectangle(3,4)
print(measure1.area(), measure1.perimeter())
