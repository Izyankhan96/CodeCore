print("Welcome to FDB Bank ATM! Please enter your PIN to continue ")
pin = input("Enter your PIN: ")
while pin != "2090":
    print("Sorry That is incorrect. Please try again 2 attempts remaining")
    pin = input("Enter your PIN: ")
print("Welcome Back MUHAMMAD! please select an option below to continue")
def get_amount(prompt):
    while True:
        amount = input(prompt).strip()
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Please enter a valid amount using numbers only (e.g. 50).")

balance = 14670
while True:
    print("Please select an option below to continue")
    print("1. WITHDRAWAL")
    print("2. DEPOSIT")
    print("3. BALANCE INQUIRY")
    print("4. EXIT")
    option = input("Enter your choice (1-4 or option name): ").strip().upper()
    if option in ("1", "WITHDRAWAL"):
        money = get_amount("Enter the amount you want to withdraw: ")
        if money > 1000:
            print("Sorry, you cannot withdraw more than $1000 at a time.")
        elif money > balance:
            print("Sorry, you do not have enough funds.")
        else:
            balance -= money
            print(f"You have successfully withdrawn ${money}.")
    elif option in ("2", "DEPOSIT"):
        money = get_amount("Enter the amount you want to deposit: ")
        balance += money
        print(f"You have successfully deposited ${money}.")
    elif option in ("3", "BALANCE INQUIRY", "BALANCE"):
        print(f"Your current balance is: ${balance}.")
    elif option in ("4", "EXIT"):
        print("Thank you for using FDB Bank ATM. Have a great day!")
        break
    else:
        print("Invalid option selected. Please try again.")