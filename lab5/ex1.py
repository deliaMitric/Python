#Create a class hierarchy for shapes, starting with a base class Shape.
# Then, create subclasses like Circle, Rectangle, and Triangle.
# Implement methods to calculate area and perimeter for each shape.
import math
class Shape:
    def area(self): pass
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, radius):
        if radius > 0:
            self._radius = radius
    def set_radius(self, radius):
        if radius > 0:
            self._radius = radius
        return "Negative radius!!!"
    def get_radius(self):
        return self._radius
    def area(self):
        circle_area = math.pi * self._radius ** 2
        return circle_area
    def perimeter(self):
        circle_perimeter = 2 * math.pi * self._radius
        return  circle_perimeter

class Rectangle(Shape):
    def __init__(self, length, width):
        if length > 0 and width > 0:
            self._length = length
            self._width = width
    def set_length(self, new_length):
        if new_length > 0 :
            self._length = new_length
        return "Negative length!!!"
    def set_width(self, new_width):
        if new_width > 0 :
            self._width = new_width
        return "Negative parameters!!!"
    def get_length(self):
        return self._length
    def get_width(self):
        return self._width
    def area(self):
        return self._length * self._width
    def perimeter(self):
        return 2 * (self._length + self._width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            self._side1 = side1
            self._side2 = side2
            self._side3 = side3
    def set_side1(self, new_side1):
        if new_side1 + self._side2 > self._side3 and new_side1 + self._side3 > self.side2  and self._side2 + self._side3 > new_side1:
            self._side1 = new_side1
        return "Invalid side for a triangle!!!"
    def set_side2(self, new_side2):
        if new_side2 + self._side1 > self._side3 and new_side2 + self._side3 > self.side1  and self._side1 + self._side3 > new_side2:
            self._side2 = new_side2
        return "Invalid side for a triangle!!!"
    def set_side3(self, new_side3):
        if new_side3 + self._side2 > self._side1 and new_side3 + self._side1 > self.side2  and self._side2 + self._side1 > new_side3:
            self._side3 = new_side3
        return "Invalid side for a triangle!!!"
    def get_side1(self):
        return self._side1
    def get_side2(self):
        return self._side2
    def get_side3(self):
        return self._side3
    def area(self):
        perimeter = self.perimeter()
        triangle_area = math.sqrt(perimeter * (perimeter - self._side1) * (perimeter - self._side2) * (perimeter - self._side3))
        return triangle_area
    def perimeter(self):
        return (self._side1 + self._side2 + self._side3) / 2

if __name__ == '__main__':
    list = [Circle(5), Rectangle(3, 5), Triangle(4, 4, 5)]
    for shape in list:
        print(shape.area())
        print(shape.perimeter())
