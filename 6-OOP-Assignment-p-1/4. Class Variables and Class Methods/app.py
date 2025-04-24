# 🏦 Bank Class with Class Variable and Class Method

class Bank:
    # Class variable
    bank_name = "Old Bank"

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    # Instance method to display bank name
    def show_bank_name(self):
        print(f"Bank Name: {self.bank_name}")

# Creating instances
account1 = Bank()
account2 = Bank()

# Showing bank name before change
print("Before changing bank name:")
account1.show_bank_name()
account2.show_bank_name()

# Changing bank name using class method
Bank.change_bank_name("New Horizon Bank")

# Showing bank name after change
print("\nAfter changing bank name:")
account1.show_bank_name()
account2.show_bank_name()
