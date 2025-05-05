# 🔢 Assignment: `callable()` and `__call__()` – Multiplier Class

## 🎯 Objective
Create a class `Multiplier` with an `__init__()` to set a factor.  
Define a `__call__()` method that multiplies an input by the factor.  
Test the class using `callable()` and by calling the object like a function.

---

## ✅ Python Code (`app.py`)

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


# Example usage
multiply_by_3 = Multiplier(3)

# Using callable() to check if the object is callable
print(callable(multiply_by_3))  # Output: True

# Calling the object like a function
result = multiply_by_3(5)
print(f"5 multiplied by factor 3 is: {result}")  # Output: 15

🧠 Explanation
__call__(): This special method allows an object to be called like a function. Here, it multiplies the given input by the factor.

callable(): The callable() function checks whether an object can be called like a function. When __call__() is defined in a class, instances of the class become callable.

🖥️ Output

True
5 multiplied by factor 3 is: 15