# Hangman Game

This is a simple implementation of the classic hangman game. The player has to guess a word by entering one letter at a time. The game is won if the player can guess all the letters in the word before they run out of tries. The game is lost if the player runs out of tries before guessing the word.

<br>

## How to Play

Run the program.
The program will select a word from a predefined list of words.
The player has to guess the word by entering one letter at a time.
If the letter is in the word, it will be revealed in the word.
If the letter is not in the word, the player will lose one try and a graphic of the hanging man will slowly form depending on how many tries you missed.
The player wins if they guess all the letters in the word before running out of tries.
The player loses if they run out of tries before guessing the word.
At the end of the game, the program will display whether the player won or lost.


![Start of the Game](/imagess/hangman.png)

when its incorrect it will show this: 

![incorrect tries hangman](/imagess/Screenshot%202023-04-16%20213950.png)



## Data Model
<br>

The Hangman game uses a simple data model that consists of the following:

word_list: a list of words that the player can choose from. This list is hardcoded into the game and contains a variety of topics ranging from computer science and technology to politics and the arts.

word: the secret word that the player needs to guess. This is selected randomly from the word_list.

tries: the number of incorrect guesses the player is allowed before they lose the game. This is set to 10 by default, but can be adjusted if desired.

unknown_word: a list of underscores that represents the unknown letters in the secret word. This list is initially empty and is populated with underscores that correspond to each letter in the secret word.

stages: a list of ASCII art that represents the different stages of the hangman drawing. This is used to display the hangman to the player as they make incorrect guesses.

Overall, the data model is simple yet effective for implementing the Hangman game. The use of hardcoded words and ASCII art may limit the variety of the game, but it makes the game easy to understand and implement.

## Testing

    I tested this project with the following test methodes
        - Passed the code though the PEP8 validator with no problems for the main code are

- __Bugs__
        - i had a bugg where you could enter a word and it would still be correct if the first letter of the word would be correct.
        - Bug where you couldnt enter any letters is Caps.



- __Exsisting Bugs__
        - the figure code to display the hangman figure didnt pass through the PEP8 validator, i had to play around with it a lot but it was impossible to get the hangman figure right with no errors in the PEP8 validator.

## Issues 

    - I have an issue with Heroku that i cant create a new app if i dont have a verified american credit card connected to my account, but since i dont live in the USA i obvously cant bind my credit card to my Heroku account with makes me unable to upload anything there.