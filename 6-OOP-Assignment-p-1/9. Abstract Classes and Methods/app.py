import streamlit as st
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method to be implemented by subclasses

# Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Streamlit UI
st.title("🔺 Abstract Classes and Methods")

# Inputs for Rectangle dimensions
length = st.number_input("Enter length of the rectangle:", min_value=1)
width = st.number_input("Enter width of the rectangle:", min_value=1)

# Create a Rectangle object and calculate area
if length and width:
    rectangle = Rectangle(length, width)
    st.success(f"Area of the rectangle: {rectangle.area()} square units")
