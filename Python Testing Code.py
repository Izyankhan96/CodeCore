# This is only to be used to Implement Test cases.
correct_username = "Izyan"
correct_password = "Izyan123"
username = input("What is your name? :")
if username == correct_username:
    password = input("Please enter your password :")
    if password == correct_password:
        print("Welcome back Izyan")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")    