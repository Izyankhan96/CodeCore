# This program is a grade checker that takes a user's name and displays their grades for three semesters.
name = input("What is your name? :")
while name != "Izyan":
    print("Sorry I dont see your name in our grading system, please try again.")
    name = input("What is your name? :")
print(f"Hello, {name} I see your name in our grading system")
student_id = input("What is your student ID? :")
while student_id != "7697623072":
    print("That is not a valid student ID, please try again.")
    student_id = input("What is your student ID? :")
print(f"Welcome back! {name} here are your grades for the three semesters.")
print("Here is your grade for semester 1 :")
grade_semester1 = 70
if grade_semester1 >= 90:
    print("A")
elif grade_semester1 >= 80:
    print("B")
elif grade_semester1 >= 70:
    print("C")
elif grade_semester1 >= 60:
    print("D")
else:
    print("F")
print("Your grade for semester 2 :")
grade_semester2 = 86
if grade_semester2 >= 90:
    print("A")
elif grade_semester2 >= 80:
    print("B")
elif grade_semester2 >= 70:
    print("C")
elif grade_semester2 >= 60:
    print("D")
else:
    print("F")
print("Your grade for semester 3 :")
grade_semester3 = 98
if grade_semester3 >= 95:
    print("A+")
elif grade_semester3 >= 90:
    print("A")
elif grade_semester3 >= 80:
    print("B")
elif grade_semester3 >= 70:
    print("C")
elif grade_semester3 >= 60:
    print("D")
else:
    print("F")

