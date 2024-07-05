class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee("Vishnu", "Kumar")

emp_1.first = "V"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

# If the first name is changes somewhere then the email never gets updated
# one way to update it is use a function like fullname() - disadv --> need to change all the email - email() tedious
# second way - use getters (i.e @property operator)

class Employee2:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # setters
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # deleter
    @fullname.deleter
    def fullname(self):
        self.first = self.last = None

emp_2 = Employee2("Test", "User")

emp_2.first = "T"

# setters
emp_2.fullname = "New User"

print(emp_2.first)
print(emp_2.email)
print(emp_2.fullname)

# deleter
del emp_2.fullname
print(emp_2.fullname)


# getter -- @property
# setter -- @function_name.setter
# deleter -- @function_name.deleter