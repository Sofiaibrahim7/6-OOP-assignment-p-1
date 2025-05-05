import streamlit as st

# Parent class
class Person:
    def __init__(self, name):
        self.name = name

# Child class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent class constructor
        self.subject = subject

    def show_info(self):
        return f"Teacher Name: {self.name} | Subject: {self.subject}"

# Streamlit app UI
st.title("👩‍🏫 Teacher Inheritance with super()")

# Example usage
teacher = Teacher("Miss Hina", "Computer Science")
st.success(teacher.show_info())
