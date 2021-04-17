# DRY  : Don't Repeat Yourself
class Mammal:
    def walk(self):
        print('Can Walk !')

    def run(self):
        print('Can Run!')

    def reproduce(self):
        print('Can Resproduce itself')


class Dog(Mammal):
    def bark(self):
        print('BHOO. BHOO !!!!')


class Cat(Mammal):
    pass


tommy = Dog()
tommy.walk()
tommy.run()
tommy.bark()

tom = Cat()
tom.reproduce()
tom.run()
