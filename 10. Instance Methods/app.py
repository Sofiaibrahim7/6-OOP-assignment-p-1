import streamlit as st

# Dog class with instance method
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"Woof! My name is {self.name} and I am a {self.breed}."

# Streamlit UI
st.title("🐶 Instance Methods - Dog Class")

name = st.text_input("Enter dog's name:")
breed = st.text_input("Enter dog's breed:")

if name and breed:
    dog = Dog(name, breed)
    st.success(dog.bark())
