# 🧪 Assignment: Access Modifiers in Python

## 🎯 Objective:
Demonstrate Public, Protected, and Private access modifiers in a Python class.

---

## 📌 Concepts:

- **Public**: Accessible from anywhere.
- **Protected (`_`)**: By convention, used for internal use (can still be accessed).
- **Private (`__`)**: Name mangled; not directly accessible outside the class.

---

## ✅ Python Code Example:

```python
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

📝 Notes:
__private_var and __private_method() are name-mangled: use internally or via special access if really needed.

_protected_var is accessible but should be respected as "for internal use".

✅ Output Example:

I am Public
Accessing public: I am Public
I am Protected
Accessing protected: I am Protected
Accessing private: I am Private