command = ""
started = False
#    '!='   ->   means: does not equal to...
while True:
    command = input("> ").lower()
    
    if command == "start":
        if started:
            print("The car is already started.")
        else:
            started = True
            print("You've successfully started the car!")
    
    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("You've stopped the car!")
    
    elif command == 'help':
        print('''
Type "start" - to start the car
Type "stop" - to stop the car
Type "quit" - to quit the game
        ''')
    
    elif command == "quit":
        break
    else:
        print("Please provide a valuable input, try again!")