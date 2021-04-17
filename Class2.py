class Employee:
    def __init__(self, fname, lname, experience, pay):
        self.fname = fname
        self.lname = lname
        self.experience = experience
        self.pay5 = pay  # left side we can assign our own values
        self.mail = fname + '.' + lname + '@employee.com'

    # each method i.e __init__ or any. -> in class take self instance as a first argument
    def full_name(self):
        return '{} {}'.format(self.fname, self.lname)


emp1 = Employee('Nishant', 'Kumbhar', 20, 50000)
emp2 = Employee('Om', 'Patil', 10, 45000)

print(emp1.mail)
print(emp2.mail)
print(emp1.pay5)
print(emp1.full_name())  # if we remove () after the name then we will get different ans i.e method
print(Employee.full_name(emp1))     # same
