# 🏦 Assignment: Class Variable and Class Method in Python

## 🎯 Objective:
Create a class `Bank` with:
- A **class variable** `bank_name`
- A **class method** `change_bank_name(cls, name)` to change the `bank_name`
Demonstrate that changing the bank name using the class method affects **all instances** of the class.

---

## 🧾 Code:

```python
class Bank:
    bank_name = "Old Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_bank_name(self):
        print(f"Bank Name: {self.bank_name}")

account1 = Bank()
account2 = Bank()

print("Before changing bank name:")
account1.show_bank_name()
account2.show_bank_name()

Bank.change_bank_name("New Horizon Bank")

print("\nAfter changing bank name:")
account1.show_bank_name()
account2.show_bank_name()


🧠 Explanation:
bank_name is a class variable shared by all instances.

@classmethod lets us change class-level data using cls.

All objects reflect the new name after using change_bank_name().

🖨 Output:

Before changing bank name:
Bank Name: Old Bank
Bank Name: Old Bank

After changing bank name:
Bank Name: New Horizon Bank
Bank Name: New Horizon Bank
✅ Result:
Class created with a class variable

Class method successfully changed the value

Change reflected in all instances