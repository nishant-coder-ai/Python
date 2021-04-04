i = 0;
while i < 10:         # while loop has bydefault else part.
    print(i)
    i = i + 1
    if i == 6:
        break       # try to comment this and upper line;
else:
    print('if while part exicuted successfully without break , then else part will be exicuted. ')
print('Done!')
