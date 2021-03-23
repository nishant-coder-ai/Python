a = 'Hello Bob'
try:
    astr = int(a)    # as this condition is blows up so, print 1,2 not executed. directly goes to except block.
    print('1')
    print('2')
except:
    astr = -1

print("First :", astr)

num = '123'
try:
    numstr = int(num)
    print('3')
    print('4')
except:
    numstr = -1
print("Second :", numstr)
