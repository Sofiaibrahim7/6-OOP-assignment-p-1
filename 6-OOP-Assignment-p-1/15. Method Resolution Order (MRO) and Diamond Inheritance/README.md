# 🔷 Assignment: MRO and Diamond Inheritance

## 🎯 Objective
Understand **Method Resolution Order (MRO)** through Diamond Inheritance.

---

## 🧱 Class Structure

- `A`: Base class with method `show()`
- `B` and `C`: Inherit from `A` and override `show()`
- `D`: Inherits from both `B` and `C`

---

## ✅ Python Code (`app.py`)

```python
class A:
    def show(self):
        return "Showing from Class A"

class B(A):
    def show(self):
        return "Showing from Class B"

class C(A):
    def show(self):
        return "Showing from Class C"

class D(B, C):  # Diamond Inheritance
    pass

# Create an object of class D
d = D()
print(d.show())

# Print the Method Resolution Order
print("MRO:", [cls.__name__ for cls in D.__mro__])

🧠 Explanation
In Diamond Inheritance, class D inherits from both B and C, which in turn inherit from A.

When d.show() is called, Python follows the MRO (left to right) as defined by C3 linearization.

So, B's version of show() is executed.

🖥️ Output

Showing from Class B
MRO: ['D', 'B', 'C', 'A', 'object']