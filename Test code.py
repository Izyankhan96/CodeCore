print("Welcome to the theme park ticket scanner")
print("Please enter your name and age to verify the age to enter")
name = input("Your name :")
age = int(input("Age :"))
if name == "Izi":
    if age >= 15:
        print("Welcome in!")
    else:
        print("No access")
else:
    print("No access")
    exit()
options = ["water slide", "castle adventure", "fast and furious ride"]
print(options)
while True:
    choice = input("So where to first? ").strip().lower()
    if choice == "water slide":
        print("The water slide is on your right. Just scan your ticket and enjoy!")
        break
    elif choice == "castle adventure":
        print("The Castle Adventure is straight down and then on your left.")
        break
    elif choice == "fast and furious ride":
        print("That will be on your left. Enjoy!")
        break
    else:
        print("Sorry, that is not one of the options. Please try again.")