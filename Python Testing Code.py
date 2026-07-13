# This is only to be used to Implement Test cases.
name = input("Enter your name: ")
while name != "Izyan":
    print("Invalid name. Please try again.")
    name = input("Enter your name: ")
print("Please enter your password below to continue")
password = input("Enter your password: ")
while password != "Izyan124":
    print("Invalid password. Please try again.")
    password = input("Enter your password: ")
print("Access granted. Welcome, Izyan!")
grade_semester1 = 90
if grade_semester1 >= 95:
    print("A+")
elif grade_semester1 >= 90:
    print("A")
elif grade_semester1 >= 85:
    print("B+")
elif grade_semester1 >= 80:
    print("B")      
elif grade_semester1 >= 75:
    print("C")
elif grade_semester1 >= 70:
    print("D")
else:
    print("F")