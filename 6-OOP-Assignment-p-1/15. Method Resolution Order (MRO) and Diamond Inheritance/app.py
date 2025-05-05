# app.py

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
