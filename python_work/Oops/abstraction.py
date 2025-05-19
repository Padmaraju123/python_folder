from practice.abc import ABC, abstractmethod

# Abstract class
class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance


# Concrete class: Savings Account
class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.04  # 4% interest

# Concrete class: Fixed Deposit Account
class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.07  # 7% interest

# Using the classes
savings = SavingsAccount(10000)
fixed = FixedDepositAccount(10000)

print("Savings Interest:", savings.calculate_interest())      # Output: 400.0
print("Fixed Deposit Interest:", fixed.calculate_interest())  # Output: 700.0
