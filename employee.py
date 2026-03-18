from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)


class PermanentEmployee(Employee):

    def __init__(self, emp_id, name, basic_salary):
        super().__init__(emp_id, name)
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = 0.2 * self.basic_salary
        da = 0.1 * self.basic_salary
        return self.basic_salary + hra + da


class ContractEmployee(Employee):

    def __init__(self, emp_id, name, pay_per_day, days):
        super().__init__(emp_id, name)
        self.pay_per_day = pay_per_day
        self.days = days

    def calculate_salary(self):
        return self.pay_per_day * self.days


# Main Program
emp_type = "Permanent"

if emp_type == "Permanent":
    emp = PermanentEmployee(1, "Arun", 40000)
else:
    emp = ContractEmployee(2, "Ravi", 1000, 20)

emp.show_details()
print("Salary:", emp.calculate_salary())