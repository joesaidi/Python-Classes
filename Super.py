
class Shape:
    def __init__(self,is_filled,color):
        self.is_filled = is_filled
        self.color = color

    def Description(self):
        return f'Color:{self.color} and  {'filled' if self.is_filled else 'not filled'}'
    
class Circle(Shape):
    def __init__(self,radius,is_filled,color):
        super().__init__(is_filled,color)
        self.radius = radius

    def Description(self):
        super().Description()
        return f'Its a circle with radius {self.radius} cm and area of {3.14*self.radius}cm^2'
    
class Square(Shape):
    def __init__(self,width,is_filled,color):
        super().__init__(is_filled,color)
        self.width = width
    
    def Description(self):
        super().Description()
        return f'Its a square with {self.width} cm and area of {self.width*self.width}cm^2'

class Triangle(Shape):
    def __init__(self,width,height,is_filled,color):
         super().__init__(is_filled,color)
         self.width = width
         self.height = height

    def Description(self):
        super().Description()
        return f'Its a triangle with width of {self.width}cm and {self.height}cm and area of {self.width*self.height/2}cm^2'
      

circle = Circle(radius=7,color='green',is_filled=False)
print(circle.Description())

triangle = Triangle(width=10,color='green',is_filled=False,height=7)
print(triangle.Description())

square = Square(width=9,color='green',is_filled=False)
print(circle.Description())
