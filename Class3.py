class Board:
    def draw(self):
        print('Draw')

    def move(self):
        print('Move')


b1 = Board()
b1.draw()
b1.x = 89
b1.y = 78
print(b1.y)
b1.move()
p2 = Board()
p2.x = 45
print(p2.x)
p2.draw()
