# 🔧 Assignment: Function Decorators – Log Function Call

## 🎯 Objective
Write a **function decorator** `log_function_call` that prints `"Function is being called"` before a function executes.  
Apply it to a function `say_hello()`.

---

## ✅ Python Code (`app.py`)

```python
# Function decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Example usage
say_hello()

🧠 Explanation
The log_function_call decorator wraps the target function and prints a message before calling it.

The @log_function_call syntax applies the decorator to say_hello.

When say_hello() is called, it first executes the wrapper() function from the decorator, then runs the original say_hello() body.

🖥️ Output

Function is being called
Hello!