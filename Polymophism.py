
from abc import ABC,abstractmethod

class Shapes:
    
    @abstractmethod
    def area(self):
        pass
    

class Circle(Shapes):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return f'Area of the circle with radius {self.radius}cm is {3.14 *self.radius **2}cm²'
        

class Square(Shapes):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return f'Area of the square with side {self.side}cm is {self.side**2}cm²'
        

class Triangle(Shapes):
    def __init__(self,base,height):
        self.height = height
        self.base = base

    def area(self):
        return f'Area of the triangle with base of {self.base}cm and {self.height}cm is {self.base *self.height/2}cm²'
    
class Ball(Circle):
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height

    def area(self):
        return f'Area of the ball with height of {self.height}cm and radius {self.radius}cm is {self.radius *self.height*2}cm²'
    
#polymophism in action 
shapes = [Circle(5),Square(5),Triangle(5,5),Ball(5,18)]

for shape in shapes:
    print(shape.area())