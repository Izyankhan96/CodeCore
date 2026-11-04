print("Welcome to the Task manager system")
name = input("Please enter your name :")
password = input("Please enter your password :")
if name == "Izi" and password == "Izi@123124":
    print("You may go once you verify your age Izi")
else:
    print("Sorry you may not proceed")
    exit()
age = int(input("Age :"))
if age >= 13:
    print("Welcome back Izi")
else:
    print("Sorry you cant proceed further")