# Class Variables

class Employee:

    # Class variable
    raise_amount = 1.04
    # access -- by instance (self.raise_amount)
    #         - by class (Employee.raise_amount)

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


emp_1 = Employee("Vishnu", "Kumar", 50000)
emp_2 = Employee("Test", "User", 20000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# accessing the instances namespace
print(emp_1.__dict__)

# accessing the class namespace
print(Employee.__dict__) # raise_amount is present only here

# accessing class variable using self will help you to modify the constant for that instance
emp_1.raise_amount = 1.10 # creates a raise_amount variable in emp_1 instance
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)

# number of emps is same for everyone so accessing using class in __init__()
# raise amount can be different for each employee so accessing using instance

emp_1.num_of_emps = 4
print(Employee.num_of_emps)
print(emp_1.num_of_emps)