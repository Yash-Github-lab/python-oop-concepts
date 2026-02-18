# Parent class
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def describe(self):
        return f"{self.name} is a {self.species}"


# Child classes inheriting from Animal
class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed
    
    # Override parent method
    def make_sound(self):
        return f"{self.name} says: Woof! Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball"


class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return f"{self.name} says: Meow! Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching the furniture"


# Usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.describe())  # Buddy is a Dog
print(dog.make_sound())  # Buddy says: Woof! Woof!
print(dog.fetch())  # Buddy is fetching the ball

print(cat.describe())  # Whiskers is a Cat
print(cat.make_sound())  # Whiskers says: Meow! Meow!
print(cat.scratch())  # Whiskers is scratching the furniture
