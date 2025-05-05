# 🧑‍🏫 8. The super() Function

## 🎯 Assignment Objective

- Create a class `Person` with a constructor that sets the name.
- Create a class `Teacher` that inherits from `Person`.
- Use `super()` to call the base class constructor.
- Add a `subject` field to the `Teacher` class.

---

## 🧠 Concept Explanation

In Python, `super()` is used to call the constructor or method of the **parent class** inside a **child class**.  
This helps avoid code duplication and allows us to extend parent functionality.

---

## ✅ Code Implementation

```python
# Parent class
class Person:
    def __init__(self, name):
        self.name = name

# Child class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling the parent class constructor
        self.subject = subject

    def show_info(self):
        return f"Teacher Name: {self.name} | Subject: {self.subject}"

# Example usage
teacher = Teacher("Miss Hina", "Computer Science")
print(teacher.show_info())

💻 Output
Teacher Name: Miss Hina | Subject: Computer Science
✅ Summary
super() is used to access the parent class's constructor and methods.

It helps in reusing code and properly initializing inherited attributes.

The child class can have additional properties while still reusing the parent class’s constructor logic.
