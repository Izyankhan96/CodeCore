import random
print("Welcome to the gussing game (no number edition)")
options = ["Easy","Medium","Hard"]
words = ["Random","Mystery","White Stone","Gate"]
words2 = ["Never","Win","Again","Try","Gain","Lose"]
words3 = ["Haha","Try again","Lol"]
print(options)
print("They will contain words like Random, Mystery, etc... You have to guess the exact word (Hint all words first word have to capital)")
choice = input("Please select an option : ")
while True:
 if choice == "Easy":
    print("Okay.")
    word = random.choice(words)
    guess = input("Guess the word : ")
    if guess == word:
        print("You guessed it!")
        break
    else:
       print("Wrong try again!")
       
 if choice == "Medium":
    print("Okay....")
    word2 = random.choice(words2)
    guess2 = input("Guess the word : ")
    if guess2 == word2:
       print("You guessed it!")
       break
    else: 
       print("Incorrect Try again!")
 if choice == "Hard":
    print("Okay............")
    word3 = random.choice(words3)
    guess3 = input("Guess the word : ")
    if guess3 == word3:
       print("You guessed it!")
       break
    else:
       print("Incorrect try again!")
