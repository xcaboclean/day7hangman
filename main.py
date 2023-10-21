import random
from replit import clear
from hangman_words import word_list
from hangman_art import stages, logo, fruits

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
print("\n*********************************")
print("Theme: Fruits Language: English")
print("*********************************")
print("\n")
print(f"{' '.join(fruits)}")
print("\n")
print(f"The word has {word_length} letters.")

#loop for read a guess
while not end_of_game:
    print(stages[lives])

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    letter_found = False
    clear()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            letter_found = True

    if not letter_found:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    if lives == 0:
        end_of_game = True
        print("You lose.")

if end_of_game:
    print(f"The word was {chosen_word}")
