# 🎩 Assignment: Class Decorators – Add Greeting to a Class

## 🎯 Objective
Create a **class decorator** `add_greeting` that modifies a class to add a method `greet()` which returns `"Hello from Decorator!"`.  
Apply it to a class `Person`.

---

## ✅ Python Code (`app.py`)

```python
# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Ali")
print(p.greet())  # Output: Hello from Decorator!

🧠 Explanation
A class decorator is a function that takes a class and returns a modified or extended version of it.

The add_greeting decorator dynamically adds a new method greet() to the class.

Using @add_greeting, we apply this decorator to Person, so now every instance of Person has a greet() method.

🖥️ Output

Hello from Decorator!