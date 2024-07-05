# Classes and Instances

class Employee:

    # Constructor
    # instance (self) is automatically passed as first argument
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee("Vishnu", "Kumar", 50000)
emp_2 = Employee("Test", "User", 20000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
# this is what happens in the background when emp_1.fullname() is called
# thats why self is always passed as first argument
print(Employee.fullname(emp_1))