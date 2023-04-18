import math
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def calculate_perimeter(self):
        return (2 * math.pi) * self.radius


    def calculate_area(self):
        return self.radius * self.radius * math.pi


class Rectangle(Shape):
    def __init__(self, height, width):
        self.width = width
        self.height = height


    def calculate_area(self):
        return self.height * self.width


    def calculate_perimeter(self):
        return (2 * self.height) + (2 * self.width)

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

