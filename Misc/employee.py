import logging

e_logger = logging.getLogger(__name__)
e_logger.setLevel(logging.INFO) # setting log level

formatter = logging.Formatter('%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
e_logger.addHandler(file_handler)

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        e_logger.info(f'Created Employee: {self.fullname}')
        
    @property
    def email(self):
        return f"{self.first} + '.' + {self.last} + '@company.com'"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"