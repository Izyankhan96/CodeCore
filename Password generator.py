import random
print("Welcome to the password generator")
characters1 = ["ABCDEFGHIJKL"]
chracters2 = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ123"]
characters3 = ["abcdefghijklmnopqrstuvwxyzABCDEFGHJKL12345!@#$"]
options = ["Easy","Medium","Hard"]
print(options)
choice = input("Please select and option : ")
while True:
 if choice == "Easy":
    print("Generating In Progress")
    one = random.choice(characters1)
    print(one)
    break
 if choice == "Medium":
   print("Generating In Progress")
   one2 = random.choice(chracters2)
   print(one2)
   break
 if choice == "Hard":
   print("Generating In Progress")
   one3 = random.choice(characters3)
   print(one3)
   break    