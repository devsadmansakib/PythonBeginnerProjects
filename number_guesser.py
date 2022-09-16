import random

print("Welcome to number guessing game!")

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print("Type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You are above the number!")
    else:
        print("You are below the number!")

print("You have tried", guesses, "times")