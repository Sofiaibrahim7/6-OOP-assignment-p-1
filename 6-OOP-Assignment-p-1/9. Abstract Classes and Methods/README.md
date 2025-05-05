# 9. Abstract Classes and Methods

## 🎯 Assignment Objective:
- Create an abstract class `Shape` with an abstract method `area()`.
- Implement the `area()` method in a `Rectangle` class that inherits from `Shape`.

---

## 🧠 Concept Explanation:
- **Abstract Class**: A class that can't be instantiated directly and requires subclasses to implement specific methods.
- **Abstract Method**: A method in an abstract class that is declared but doesn't contain any implementation. Subclasses must provide an implementation.

---

## ✅ Code Implementation

```python
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # This method should be implemented in subclasses

# Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create an object of Rectangle
rectangle = Rectangle(5, 3)

# Show the area of the rectangle
print(f"Area of the rectangle: {rectangle.area()} square units")

💻 Expected Output:
Area of the rectangle: 15 square units

✅ Summary:
Abstract classes and methods provide a way to define common interfaces for subclasses while allowing each subclass to implement its own logic.

The abc module in Python is used to create abstract base classes and define abstract methods.


