# 🧮 Assignment: Static Methods in Python

## 🎯 Objective:
Create a class `MathUtils` with:
- A **static method** `add(a, b)` that returns the sum of two numbers.
- **No class or instance variables** should be used.

---

## 🧾 Code:

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Using the static method without creating an object
result = MathUtils.add(10, 5)
print("Sum is:", result)

🧠 Explanation:
@staticmethod decorator allows defining a method that doesn't use self or cls.

We can call the method directly using the class name: MathUtils.add(10, 5)

No instance or class variables are needed.

🖨 Output:

Sum is: 15
✅ Result:
We successfully:

Created a static method

Called it without using any class or instance variables