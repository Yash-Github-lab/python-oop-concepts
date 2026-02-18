from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses"""
        pass


class Rectangle(Shape):
    """Rectangle implementation"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle implementation"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Triangle(Shape):
    """Triangle implementation"""
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c


# Polymorphic function
def print_shape_info(shape):
    """Works with any Shape subclass"""
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print()


# Usage - same function works with different shape types
rectangle = Rectangle(5, 10)
circle = Circle(7)
triangle = Triangle(3, 4, 5)

print("Rectangle:")
print_shape_info(rectangle)

print("Circle:")
print_shape_info(circle)

print("Triangle:")
print_shape_info(triangle)
