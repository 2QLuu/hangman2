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
            if char == word[i]:
                unknown_word[i] = char

    else: 
        trys -= 1
        print(f"trys remaining {trys}")
        


    if "_" not in unknown_word:
        print("winner! you won")
        break
    elif trys <= 0:
        print("you lost!")
        break    

