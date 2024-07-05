# Inheritance - Creating Subclasses

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# Developer class
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) both are same useful in multiple inheritance
        self.prog_lang = prog_lang

# Manager class
class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--> {}".format(emp.fullname()))


emp_1 = Employee("Vishnu", "Kumar", 50000)
emp_2 = Employee("Test", "User", 30000)

dev_1 = Developer("Test", "1", 50000, "Python")
dev_2 = Developer("Test", "2", 30000, "Java")

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mng_1 = Manager("Mngr", "1", 100000, [dev_1])

mng_1.add_emp(dev_2)
mng_1.print_emps()

mng_1.remove_emp(dev_1)
mng_1.print_emps()

# print(help(Developer)) --> gives the details of the class and method resolution order

# checks whether an instance is object of its class
print(isinstance(dev_1, Developer))
print(isinstance(dev_1, Employee))
print(isinstance(dev_1, Manager))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))