#if
#and
#or
#not

#elif
#else



#This is for the "and" statement

income = int(input('Your monthly-income: '))
credit = int(input('Your credit-score: '))
if income > 2500 and credit > 2:
    print("Eligible for loan")


else:
    print("Not eligible for loan")

#this is for the "or" statement

Height = float(input('What is your current height?: '))
Weight = float(input('What is your current weight?: '))
if Height > 1.88 or Weight > 65 and Weight < 90:
    print("Able to ride in rollercoaster")

else:
    print("Do not enter")