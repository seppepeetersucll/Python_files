Price = 1000000
No_credit = True
Have_credit = False

if No_credit:
    print("Your upfont downpayment wil be 20%...")
    down_payment = 0.2 * Price
elif Have_credit:
    print("You have a good credit-score, your down-payment will be 10%.")
    down_payment = 0.1 * Price


print(f"Down payment: €{down_payment}")
print("Goodluck with your journey!")