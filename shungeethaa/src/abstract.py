from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    
    @abstractmethod
    def move(self):
        pass

# Concrete class: Bird
class Bird(Animal):
    def move(self):
        print("Bird flies in the sky.")

# Concrete class: Fish
class Fish(Animal):
    def move(self):
        print("Fish swims in the water.")

# Concrete class: Dog
class Dog(Animal):
    def move(self):
        print("Dog runs on land.")

# Using the Animal classes
animals = [Bird(), Fish(), Dog()]

for animal in animals:
    animal.move()
