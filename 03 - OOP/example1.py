import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @abstractmethod
    def area(self):
        pass    


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)

        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
    
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)

        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

    def area(self):
        return self.radius ** 2 *  math.pi

class Shapes:
    def __init__(self, shapes=None):
        shapes = [] if shapes is None else shapes
        self._shapes = shapes
    
    def add_new_shape(self, shape):
        self._shapes.append(shape)

    def area_of_all_rectangles(self):
        return self.__area_of(Rectangle)
    
    def area_of_all_circle(self):
        return self.__area_of(Circle)

    def __area_of(self, shape_type):
        result = 0
        for shape in self._shapes:
            if isinstance(shape, shape_type):
                result += shape.area
        
        return result

    def __getitem__(self, index):
        return self._shapes[index]
