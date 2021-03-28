hours = input("Enter the Hours : ")
rate = input("Enter the Rate Per Hour : ")
try:
    hrs = float(hours)
    r = float(rate)
except:
    print("Please Input a Valid Number !")
    quit()

if hrs <= 40:
    xp = hrs * r
else:
    normal = hrs * r
    overtime = (hrs - 40 ) * (0.5 * r)
    xp = normal + overtime

print(xp)