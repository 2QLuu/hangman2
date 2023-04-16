import random

word_list = ["python", "programming", "hangman", "game", "computer"]

word = random.choice(word_list)

character = input("guess: ")

if character in word:
    print("correct")
else: print("incorrect")
