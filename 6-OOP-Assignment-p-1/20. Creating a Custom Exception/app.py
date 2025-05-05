# app.py

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
