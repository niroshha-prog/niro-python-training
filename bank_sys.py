from abc import ABC, abstractmethod

# 1. Abstraction
class BankAccount(ABC):
    def __init__(self, name, balance):
        self.name = name
        # 2. Encapsulation
        self._balance = balance 

    @abstractmethod
    def calculate_interest(self):
        pass

    def display_details(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self._balance}")

# 3. Inheritance
class SavingsAccount(BankAccount):
    
    # 4. Polymorphism
    def calculate_interest(self):
        interest = self._balance * 0.05
        print(f"Interest Earned: {interest}")
        return interest