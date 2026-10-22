print("Welcome to FDB Bank ATM! Please enter your PIN to continue")
pin = input("Enter your PIN: ")
while pin != "2090":
    print("Sorry, that is incorrect. Please try again.")
    pin = input("Enter your PIN: ")
print("Welcome Back MUHAMMAD!")

balance = 14670
options = ["1", "2", "3", "4"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
option = ""

while option != "4":
    print("Please select an option below to continue")
    print("1. WITHDRAWAL")
    print("2. DEPOSIT")
    print("3. BALANCE INQUIRY")
    print("4. EXIT")
    option = input("Enter your choice (1-4): ")
    while option not in options:
        print("Invalid option selected. Please choose 1, 2, 3 or 4.")
        option = input("Enter your choice (1-4): ")

    if option == "1":
        is_number = False
        while not is_number:
            amount = input("Enter the amount you want to withdraw: ")
            is_number = True
            if amount == "":
                is_number = False
            i = 0
            while i < len(amount):
                if amount[i] not in digits:
                    is_number = False
                i = i + 1
            if not is_number:
                print("Please enter the amount using numbers only (e.g. 50).")
        money = int(amount)
        if money <= 0:
            print("Please enter an amount greater than $0.")
        elif money > 1000:
            print("Sorry, you cannot withdraw more than $1000 at a time.")
        elif money > balance:
            print("Sorry, you do not have enough funds.")
        else:
            balance = balance - money
            print(f"You have successfully withdrawn ${money}.")
    elif option == "2":
        is_number = False
        while not is_number:
            amount = input("Enter the amount you want to deposit: ")
            is_number = True
            if amount == "":
                is_number = False
            i = 0
            while i < len(amount):
                if amount[i] not in digits:
                    is_number = False
                i = i + 1
            if not is_number:
                print("Please enter the amount using numbers only (e.g. 50).")
        money = int(amount)
        if money <= 0:
            print("Please enter an amount greater than $0.")
        else:
            balance = balance + money
            print(f"You have successfully deposited ${money}.")
    elif option == "3":
        print(f"Your current balance is: ${balance}.")
    else:
        print("Thank you for using FDB Bank ATM. Have a great day!")
