num = input("Enter Your Age : ")
try:
    age = int(num)
except:
    age = -1

if age >= 0:
    print("Welcome !")
else:
    print("Please Enter a valid Age ! ")
