  # 🐶 10. Instance Methods

## 🎯 Assignment Objective:
- Create a class `Dog` with instance variables `name` and `breed`.
- Add an instance method `bark()` that prints a message including the dog's name.

---

## 🧠 Concept Explanation:

- **Instance Variables** are variables tied to a specific object. Each object has its own copy.
- **Instance Methods** are functions defined in a class that operate on the instance (object) via `self`.

---

## ✅ Code Implementation

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"Woof! My name is {self.name} and I am a {self.breed}."

▶️ Example Usage:
dog = Dog("Rex", "Labrador")
print(dog.bark())

💻 Output:
Woof! My name is Rex and I am a Labrador.
