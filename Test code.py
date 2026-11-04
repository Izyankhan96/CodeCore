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