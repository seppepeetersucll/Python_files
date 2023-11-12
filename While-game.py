#build a guessing game, guess the right numer. 3 CHANCES ONLY!!

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You've won!")
        break
else:
    print("Sorry, you failed...")
