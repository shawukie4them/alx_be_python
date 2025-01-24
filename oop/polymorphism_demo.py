import math

class Shape:
    """Base class for shapes"""
    def area(self):
        """Raise an error to enforce method override"""
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """Rectangle shape with length and width"""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle"""
        return self.length * self.width

class Circle(Shape):
    """Circle shape with radius"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return math.pi * self.radius ** 2