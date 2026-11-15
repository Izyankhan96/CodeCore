import random
print("Welcome to the password generator")
characters1 = "ABCDEFGHIJKL"
characters2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123"
characters3 = "abcdefghijklmnopqrstuvwxyzABCDEFGHJKL12345!@#$"
options = ["Easy", "Medium", "Hard"]
print(options)

choice = input("Please select an option : ").strip().capitalize()
while choice not in options:
    print("That's not a level. Please type Easy, Medium or Hard.")
    choice = input("Please select an option : ").strip().capitalize()

if choice == "Easy":
    characters = characters1
    length = 8
elif choice == "Medium":
    characters = characters2
    length = 12
else:
    characters = characters3
    length = 16

print("Generating In Progress")
password = ""
i = 0
while i < length:
    password = password + random.choice(characters)
    i = i + 1
print(f"Your password is: {password}")
