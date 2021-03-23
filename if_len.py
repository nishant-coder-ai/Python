name = input("Enter the Name : ")
if len(name) < 4:
    print("Name Must be Minimum 4 Character Long.")
elif len(name) >= 10:
    print("Name Must be Maximum 10 Character Long.")
else:
    print("Correct !")
