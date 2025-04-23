# 🔢 Python Class Assignment – Using `cls` and Class Variables

## 📘 Topic: Tracking Object Count with Class Variable and Class Method

In Python, **class variables** are shared by all objects of the class. You can use them when you want to maintain a **single shared value** for all instances.

To access and modify class variables, **class methods** are used with the `@classmethod` decorator and `cls` keyword.

---

## 📝 Assignment Objective:

> Create a class `Counter` that keeps track of how many objects have been created. Use a **class variable** and a **class method** with `cls` to manage and display the count.

---

## ✅ Python Code:

```python
class Counter:
    # Class variable to track the number of objects
    count = 0

    def __init__(self):
        # Increment the count every time a new object is created
        Counter.count += 1

    # Class method to display the current count
    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Creating multiple objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Displaying the object count
Counter.display_count()

💡 Sample Output:
Total objects created: 3


🔍 Explanation:

Concept	Description
count	A class variable that is shared among all instances of Counter
__init__()	A constructor method that increments the count every time an object is made
@classmethod	A decorator that makes display_count() a class method
cls	Refers to the class itself, just like self refers to the object
✅ Summary:
Class variables are used to share data across all instances.

cls is used in class methods to access these shared variables.

This is useful when tracking how many objects have been created from a class.