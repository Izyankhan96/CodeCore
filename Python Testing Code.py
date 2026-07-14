# This is only to be used to Implement Test cases.
name = input("Please Enter your name: ")
while name != "Aiza":
    print("Invalid name Please try again.")
    name = input("Please enter your name: ")
print("Please enter your password below to continue.")
password = input("Please Enter your password: ")
while password != "Aiza123":
    print("Invalid Password Please try again.")
    password = input("Please enter your password: ")
print("Welcome back Aiza! Access granted.")
print("Here is your grade for this semester :")
grade = 90
if grade >= 95:
    print("A+")
elif grade >= 90:
    print("A")
elif grade >= 85:
    print("B+")
elif grade >= 80:
    print("B")
elif grade >= 75:
    print("C+")
elif grade >= 70:
    print("C")  
else:
    print("F")