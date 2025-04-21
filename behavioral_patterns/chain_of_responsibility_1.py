# Abstract Base Class (ABC) and Abstract Method
# Abstract Base Class (ABC) is a class that cannot be instantiated on its own and is meant to be subclassed.

from abc import ABC, abstractmethod
 

class Shape(ABC):    #  --> This is a special kind of blueprint – abstract base class
  @abstractmethod    #  --> Decorator that you can use to declare abstract methods within an abstract base class
  def area(self):
    pass             #  --> '''An abstract method has no implementation in the abstract base class.
                     #      It serves as a blueprint or a requirement that all concrete subclasses
                     #      of Shape must provide their own specific implementation for the area method.'''

 

class Circle(Shape):          #  --> This line defines a class named Circle that inherits from the Shape class. This means that Circle is a concrete subclass of Shape.
  def __init__(self, radius): #  --> This is the constructor of the Circle class. It's called when you create a Circle object.
    self.radius = radius
 

  def area(self):                           #  --> This method overrides the abstract area method from the Shape class.
    return 3.14 * self.radius * self.radius
 

class Square(Shape):
  def __init__(self, side):
    self.side = side
 

  def area(self):
    return self.side * self.side
  
  
# -----------------------------------------
# Create objects
circle = Circle(5)
square = Square(4)

# Calculate areas
print(circle.area())  # Output: 78.5
print(square.area())  # Output: 16
# -----------------------------------------



# ---------------------------------------------------------------------------------
shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(shape.area())  # Calls the overridden method specific to each subclass
# ---------------------------------------------------------------------------------


# Overridden implementations



#                              Key Characteristics of Overriding
#                             -----------------------------------
# 1) Same Method Signature: The subclass method must have the same name and parameters as the superclass method.
# 2) Inheritance Required: Overriding only occurs in an inheritance hierarchy (subclass vs. superclass).
# 3) Dynamic Binding: The method that gets executed is determined at runtime based on the object type.




#                   Shape (Superclass)
#                   ▲
#                   │ (Inheritance)
#                   │
#           +-------+-------+
#           │               │
#         Circle          Square
#           │               │
#           ▼               ▼
#           area()          area()   (Concrete Subclass (Overriding the Method))