name = input("What is your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters, try again.")

elif len(name) > 20:
    print("Ma, uw make, Pi! Da mag hier ma 20 tekens max zijn eh moat!")

else:
    print("That's a beautifull name " + name + "!")