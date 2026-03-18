from abc import ABC, abstractmethod

# 4. Vehicle Rental System
class Vehicle(ABC):
    @abstractmethod
    def rent(self, days): pass

class Car(Vehicle):
    def rent(self, days): return days * 1000

class Bike(Vehicle):
    def rent(self, days): return days * 500

# 5. Online Payment System
class Payment(ABC):
    @abstractmethod
    def pay(self, amount): pass

class UPI(Payment):
    def pay(self, amount): print(f"Paid {amount} using UPI.")

class Card(Payment):
    def pay(self, amount): print(f"Paid {amount} using Card.")             
def run_system():
    # Rental Input
    v_type, days = "Car", 3
    vehicle = Car() if v_type == "Car" else Bike()
    total = vehicle.rent(days)
    print(f"Vehicle: {v_type}\nDays: {days}\nTotal Rent: {total}")
    
    # Payment Input
    p_mode, p_amt = "UPI", total
    print(f"\nPayment Mode: {p_mode}\nAmount: {p_amt}")
    pay_method = UPI() if p_mode == "UPI" else Card()
    pay_method.pay(p_amt)

if __name__ == "__main__":
    run_system()