import random

word_list = ["python", "programming", "hangman", "game", "computer"]

word = random.choice(word_list)

trys = 10

unknown_word = []

for i in range(0, len(word)):
    unknown_word.append('_')

print(word)
print(unknown_word)

while True:
    print(unknown_word)
    char = input("guess: ")

    if char in word:
        print("correct")
        for i in range(0, len(word)):
            print(char, word[i])
            if char == word[i]:
                unknown_word[i] = char

    else: 
        print("incorrect")
        trys -= 1
