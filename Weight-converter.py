Weight = int(input("What is your weight?: "))
Ask_weight = input("Is this in (L)bs or (K)g?: ")

if Ask_weight.upper() == 'L':
    converted_weight = Weight * 0.45
    print("You are {:.2f} kilogram".format(converted_weight))

elif Ask_weight.upper() == 'K':
    converted_weight = Weight / 0.45
    print("You are {:.2f} pounds".format(converted_weight))

else:
    print("Invalid input. Please enter 'L' for pounds and 'K' for kilogram")

