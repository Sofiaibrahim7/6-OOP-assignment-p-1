# 🚗 Assignment 3: Public Variables and Methods in Python

## 🎯 Objective:
Create a class `Car` with:
- A **public variable** `brand`
- A **public method** `start()`
Then:
- Instantiate the class
- Access both the variable and the method **from outside the class**

---

## 🧾 Code:

```python
# Class definition
class Car:
    # Constructor with public variable
    def __init__(self, brand):
        self.brand = brand  # Public variable

    # Public method
    def start(self):
        print(f"{self.brand} is starting...")

# Creating an object of the class
my_car = Car("Toyota")

# Accessing the public variable
print("Car brand:", my_car.brand)

# Accessing the public method
my_car.start()

🧠 Explanation:
class Car:
This defines a new class named Car.

def init(self, brand):
This is the constructor that runs when an object is created. It takes brand as a parameter and assigns it to a public variable self.brand.

self.brand = brand:
brand is a public variable, which means it can be accessed from outside the class.

def start(self):
This is a public method named start. It prints a message showing the car is starting.

my_car = Car("Toyota")
Here we create an object of the Car class with brand Toyota.

print(my_car.brand)
This line accesses the public variable from outside the class.

my_car.start()
This line calls the public method from outside the class.

🖨 Output:

Car brand: Toyota
Toyota is starting...
✅ Result:
We successfully:

Created a class with public variable and method

Accessed both from outside the class