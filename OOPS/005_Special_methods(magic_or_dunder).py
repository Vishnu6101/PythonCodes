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
        self.pay = self.pay * self.raise_amt

    # dunder methods --> contains __xyz__()
    def __repr__(self):
        return 'Employee ({}, {}, {})'.format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    def __eq__(self, other):
        return self.pay == other.pay

emp_1 = Employee("Vishnu", "Kumar", 50000)
emp_2 = Employee("Test", "User", 20000)

print(emp_1) # calls the __str__() if it is not present it calls __repr__()

print(repr(emp_1)) # or print(emp_1.__repr__())
print(str(emp_1)) # or print(emp_1.__str__())

# repr is mainly used for developers info and str is mainly used for end user info

# operator overloading
print(1 + 2, int.__add__(1,2))
print('a' + 'b', str.__add__('a', 'b'))

print(emp_1 + emp_2)

# length
print(len("vishnu"), "vishnu".__len__())
print(len(emp_1))

# https://docs.python.org/3/reference/datamodel.html#special-method-names
# comparision operators
print(emp_1 == emp_2)