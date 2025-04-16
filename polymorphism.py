class Animal:
    def move(self):
        print("This animal moves.")

class Dog(Animal):
    def move(self):
        print("The dog runs and barks! 🐕")

class Fish(Animal):
    def move(self):
        print("The fish swims fast. 🐠")

class Bird(Animal):
    def move(self):
        print("The bird flies in the sky. 🐦")

# Demonstration of polymorphism
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal.move()