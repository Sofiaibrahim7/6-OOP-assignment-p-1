
class AccessDemo:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I am Private"

    def public_method(self):
        return f"Accessing public: {self.public_var}"

    def _protected_method(self):
        return f"Accessing protected: {self._protected_var}"

    def __private_method(self):
        return f"Accessing private: {self.__private_var}"

    def access_private_inside(self):
        return self.__private_method()  # Accessible inside class

# Create object
obj = AccessDemo()

# Accessing public
print(obj.public_var)            # ✅ Works
print(obj.public_method())       # ✅ Works

# Accessing protected
print(obj._protected_var)        # ⚠️ Works but not recommended
print(obj._protected_method())   # ⚠️ Works but should be treated as internal

# Accessing private
# print(obj.__private_var)       # ❌ Error
# print(obj.__private_method())  # ❌ Error
print(obj.access_private_inside())  # ✅ Correct way
