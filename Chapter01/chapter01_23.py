import time 
import csv
import random

if __name__ == "__main__":
    name = input("What is your name")
    print(f"Hi {name} Time to play game")
    print()

    time.sleep(1)
    print("Start loading")
    time.sleep(1)
    words = []

    with open('./Chapter01/Chapter01_resource/word_list.csv', "r") as f :
        reader = csv.reader(f)
        next(reader)
        for c in reader:
            words.append(c)
            print(c)
    random.shuffle(words)
    q = random.choice(words)
    # word = "secret"
    word = q[0]
    guesses = ''

    turns = 10 

    while turns > 0 :
        print(f"count {turns}")
        print(f"Hint {q[1].strip()}")
        failed = 0 

        for char in word:
            if char in guesses:
                print(char, end='')
            else :
                print("_", end='')
                failed += 1 

        if failed == 0 : 
            print()
            print()
            print("Congratulations! The Guesses is correct")
            break 
        print()
        guess = input("Guess the word")
        guesses += guess 

        if guess not in word : 
            turns -= 1 
            print("Fail!")
            print(f"You have {turns} more guesses!")
        
            if turns == 0 : 
                print("Fail! Bye")


