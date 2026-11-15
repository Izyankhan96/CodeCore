import random

print("Hello! Welcome to the Multi-Try guessing game with difficulty levels")
options = ["Easy", "Medium", "Hard"]
print(options)

while True:
    choice = input("Please select what level you would like to play on: ").strip().capitalize()
    if choice == "Easy":
        highest = 10
        break
    elif choice == "Medium":
        highest = 50
        break
    elif choice == "Hard":
        highest = 100
        break
    else:
        print("Not a valid level. Please type Easy, Medium or Hard.")

number = random.randint(1, highest)
tries = 0
print("I'm thinking of a number between 1 and", highest)

while True:
    guess = input("Guess the number: ").strip()
    if not guess.isdigit():
        print("Please type a whole number.")
        continue
    answer = int(guess)
    tries = tries + 1
    if answer == number:
        print("You guessed it in", tries, "tries!")
        break
    else:
        print("That's incorrect, try again.")
