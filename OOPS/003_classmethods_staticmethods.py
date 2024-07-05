# Class Methods and Static methods

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        '''checks whether the given day is a weekday'''
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp_1 = Employee("Vishnu", "Kumar", 50000)
emp_2 = Employee("Test", "User", 20000)

# class methods take class as the first argument
Employee.set_raise_amt(1.05) # it updates the class variable value

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# can be accessed via an instance
# emp_1.set_raise_amt(1.1)

# ----------------------------------------------------------------
# Alternative constructors
# using class methods as alternative constructors

emp_str_1 = "Vishnu-kumar-50000"
emp_str_2 = "Test-user-10000"

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_1.pay)

# ------------------------------------------------------------
# Static methods - dont operate on the instance of the class
# no automatic first argument, use it when the methods does not uses any class or instance variable
import datetime
date = datetime.date(2024, 1, 2)
print(Employee.is_workday(date))
print(emp_1.is_workday(date))

# Regular instance methods - takes instance as first arg
# class methods - takes class as first arg
# static methods - does not take any default first arg