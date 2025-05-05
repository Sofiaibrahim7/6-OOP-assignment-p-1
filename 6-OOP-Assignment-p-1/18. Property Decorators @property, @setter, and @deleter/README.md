# 🏷️ Assignment: Property Decorators – @property, @setter, and @deleter

## 🎯 Objective
Create a class `Product` with a private attribute `_price`.  
Use **@property** to get the price, **@price.setter** to update it, and **@price.deleter** to delete it.

---

## ✅ Python Code (`app.py`)

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price")
        del self._price


# Example usage
product = Product(100)

print("Price:", product.price)  # Get price using @property

product.price = 120  # Set price using @price.setter
print("Updated Price:", product.price)

del product.price  # Delete price using @price.deleter
