command = ""
print("Enter help to continue....")
started = False
while True:
    command = input(">>>").lower()
    if command == "start":
        if started:
            print("Car is Already Started ! :) ")
        else:
            started = True
            print("Car Started ----->")
    elif command == "stop":
        if not started:
            print("Car is Already Stopped ! :(")
        else:
            started = False
            print("Car Stopped |_|")
    elif command == "help":
        print('''
        start --> To start the car.
        stop  --> To stop the car.
        quit  --> To quit the Game.
        ''')
    elif command == "quit":
        break
    else:
        print("Unable to find Command , Try it again !")
