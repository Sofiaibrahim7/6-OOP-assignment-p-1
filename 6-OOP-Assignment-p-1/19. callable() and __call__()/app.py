# app.py

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
