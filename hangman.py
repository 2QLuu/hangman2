import random

word_list = [
    "python", "programming", "hangman", "game", "computer", "science",
    "engineering", "mathematics", "physics", "chemistry", "biology",
    "medicine", "history", "geography", "artificial", "intelligence",
    "machine", "learning", "data", "analysis", "visualization",
    "natural", "language", "processing", "network", "security",
    "cybersecurity", "cryptography", "algorithms", "data", "structures",
    "operating", "systems", "software", "engineering", "web", "development",
    "mobile", "applications", "cloud", "computing", "internet", "of", "things",
    "robotics", "automation", "virtual", "reality", "augmented", "reality",
    "blockchain", "distributed", "systems", "cryptocurrencies", "quantum",
    "computing", "nanotechnology", "biotechnology", "genetics", "climate",
    "change", "sustainability", "renewable", "energy", "politics", "economics",
    "finance", "marketing", "sales", "customer", "service", "leadership",
    "management", "entrepreneurship", "innovation", "creativity", "design",
    "user", "experience", "psychology", "philosophy", "religion", 
    "spirituality"
]


word = random.choice(word_list)

trys = 10

unknown_word = []

for i in range(0, len(word)):
    unknown_word.append('_')


while True:
    print(unknown_word)
    char = input("guess: ").lower()

    if len(char) != 1:
        print("Please enter only one letter!")
        continue

    if char in word:
        print("correct")
        for i in range(0, len(word)):
            if char == word[i]:
                unknown_word[i] = char

    else: 
        print('incorrect!')
        trys -= 1
        print(f"trys remaining {trys}")
        


    if "_" not in unknown_word:
        print("winner! you won")
        break
    elif trys <= 0:
        print("you lost!")
        break    

