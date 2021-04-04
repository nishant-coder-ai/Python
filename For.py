for i in 'Lexcrop industries':
    print(i)
print('////////////////////////////////////////')
for item in ['Nishant', 'Prasad', 'Sarang', 'Raj', 'Rutwik']:
    print(item)
print('////////////////////////////////////////')
for j in range(10):
    print(j)              # print 0 to 9;
print('////////////////////////////////////////')
for k in range(5, 10):
    print(k)              # print 5 to 9;
print('////////////////////////////////////////')
for z in range(1, 20, 2):
    print(z)              # print all odd numbers from 1 to 20
print('////////////////////////////////////////')
sum_of_p = 0
for s_l in [20, 30, 40]:
    sum_of_p = sum_of_p + s_l
print(sum_of_p)
print('////////////////////////////////////////')
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    for i in range(item):
        print("X", end="")
    print("")
