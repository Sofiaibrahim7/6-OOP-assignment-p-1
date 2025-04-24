# Class definition
class Car:
    # Public variable
    def __init__(self, brand):
        self.brand = brand

    # Public method
    def start(self):
        print(f"{self.brand} is starting...")

# Instantiating the class
my_car = Car("Toyota")

# Accessing the public variable
print("Car brand:", my_car.brand)

# Calling the public method
my_car.start()
