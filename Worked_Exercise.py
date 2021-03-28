count = 0
sum_of_num = 0.0

while True:
    num = input("Enter the Numbers : ")
    if num == 'done' or num == 'Done':
        break
    try:
        f_num = float(num)
    except:
        print("Invalid Input ! ")
        continue
    count = count + 1
    sum_of_num = sum_of_num + f_num

print("All Done ")
print(count, sum_of_num)
