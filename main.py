import random
from hangman_words import word_list
from hangman_art import stages,logo

print(logo)

end_of_game = False
lives = 6
letter_found = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


#Create blanks
display = []
for _ in range(word_length):
  display += "_"

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
