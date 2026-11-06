print("Hello Welcome to the Multi-Try guessing game with diffuculty levels")
options = ["Easy","Medium","Hard"]
print(options)
import random
while True:
    choice = input("Please select what level you would like to play on")
    if choice == "Easy":
        number = random.randint(1, 10)
        print(number)
        answer = int(input("Guess the number :"))
        if answer == number:
            print("You guessed it!")
            break
        if choice == "Medium":
            number_2 = random.randint(1, 50)
            print(number_2)
            answer_2 = int(input("Guess the number : "))
            if answer_2 == number_2:
                print("You guessed it")
                break
            if choice == "Hard":
                number_3 = random.randint(1, 100)
                print(number_3)
                answer_3 = int(input("Guess the number : "))
                if answer_3 == number_3:
                    print("You guessed it!")
                    break
        else:
            print("Thats incorrect")