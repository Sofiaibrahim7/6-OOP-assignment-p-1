# app.py

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
