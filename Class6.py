class Point:
    def __init__(self, jack, tom, ria, jerry):
        self.ajack = jack         # here we assign jack,tom, ria, jerry value to ajack, aria, atom , ajerry
        self.atom = tom           # and then these variables are acssible .
        self.aria = ria
        self.ajerry = jerry
        print('Hi')                 # but we cannot return a value from constructor

    def printout(self, name):
        print(self.atom)
        print(self.ajack)
        print(self.ajerry)
        print(self.aria)
        print(name)


p1 = Point(3, 'Four', True, 78)
print(p1.aria)
print(p1.ajerry)
print(p1.atom)
print(p1.ajack)
p1.printout('Nishant')
