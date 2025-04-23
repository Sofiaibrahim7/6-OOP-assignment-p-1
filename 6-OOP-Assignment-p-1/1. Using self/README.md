# 🧑‍🎓 Python Class Assignment – Using `self` Keyword

## 📘 Topic: Understanding the `self` Keyword in Python

In Python, `self` is a reference to the current instance of the class. It is used to access variables and methods within the class. Whenever we create an object of a class, `self` allows that object to store its own data independently from other objects.

### 🔍 Why use `self`?
- It helps differentiate between **instance variables** and **local variables**.
- It allows each object to maintain its own state.
- It must be the **first parameter** of instance methods in a class.

---

## 📝 Assignment Objective:

> Create a class `Student` with attributes `name` and `marks`. Use the `self` keyword to initialize these values via a constructor. Add a method `display()` that prints student details.

---

## ✅ Python Code:

```python
class Student:
    # Constructor to initialize name and marks
    def __init__(self, name, marks):
        self.name = name      # 'self.name' is an instance variable
        self.marks = marks    # 'self.marks' is also an instance variable

    # Method to display student details
    def display(self):
        print("\n--- Student Details ---")
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")

# User input
name_input = input("Enter student name: ")
marks_input = int(input("Enter marks: "))

# Creating object and calling method
student1 = Student(name_input, marks_input)
student1.display()
