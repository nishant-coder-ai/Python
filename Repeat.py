# if we want to run program infinite times unless and until user ends it , then --->
# we use True in while Loops , and it ends when break is executed.

command = ''
while True:
    command = input(">>>").lower()
    if command == 'help':
        print("Thanks For Asking Help !")
        print("Please Type run as a Command.")
        print("Use quit command to exit.")
    elif command == 'run':
        a = int(input("Enter the number  : "))
        sqr = a * a
        print("Square of Entered Number is : ", sqr)
    elif command == 'quit':
        break
    else:
        print("Unable to Find Command , Try Again !")
