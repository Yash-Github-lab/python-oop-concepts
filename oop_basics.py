# Basic Class Definition
class Person:
    # A class to represent a person
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Initialize person attributes
        self.name = name  # Instance variable
        self.age = age    # Instance variable
    
    # Instance method
    def greet(self):
        # Method to greet
        return f"Hello, I'm {self.name} and I'm {self.age} years old"
    
    # Another method
    def have_birthday(self):
        # Increment age by 1
        self.age += 1
        return f"{self.name} is now {self.age} years old"


# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.greet())  # Hello, I'm Alice and I'm 25 years old
print(person2.greet())  # Hello, I'm Bob and I'm 30 years old
print(person1.have_birthday())  # Alice is now 26 years old
