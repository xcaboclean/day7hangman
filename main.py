    #Step 4

import random

stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

end_of_game = False
lives = 6
letter_found = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Create blanks
display = []
for _ in range(word_length):
  display += "_"

#Testing code
print(f"Psst, the solution is {chosen_word}.")
#loop for read a guess
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  letter_found = False
  
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    print(f"Current position:{position}\nCurrent letter:{letter}\nGuessed letter:{guess}")
    if letter == guess:
      display[position] = letter
      letter_found = True
  print(display)
  
  if not letter_found: 
    lives -= 1
    print(display)
    print(stages[lives])
    
  if "_" not in display:
    end_of_game = True
    print("You win.")
  
  if lives == 0:
    end_of_game = True
    print("You lose.")
    
    #TODO-3: - print the ASCII art from 'stages' thae aí, mulheres...t corresponds to the current number of 'lives' the user has remaining.