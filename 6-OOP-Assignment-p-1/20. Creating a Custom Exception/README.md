# 🚫 Assignment: Creating a Custom Exception – InvalidAgeError

## 🎯 Objective
Create a custom exception `InvalidAgeError`.  
Write a function `check_age(age)` that raises this exception if `age < 18`.  
Handle the exception using `try...except`.

---

## ✅ Python Code (`app.py`)

```python
# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age is less than 18, which is invalid")
    return "Age is valid"

# Example usage
try:
    age = 16
    print(check_age(age))
except InvalidAgeError as e:
    print(f"Error: {e}")

🧠 Explanation
Custom Exception: We define a custom exception InvalidAgeError that inherits from Python’s built-in Exception class.

check_age() function: This function checks if the age is less than 18, and if so, raises the custom exception.

try...except: We handle the raised exception in the except block and print the error message.

🖥️ Output

Error: Age is less than 18, which is invalid
