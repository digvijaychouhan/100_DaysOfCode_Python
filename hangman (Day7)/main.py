# Hangman 
import random
from hangman_art import stages, logo
from hangman_words import word_list

# Print Hangman logo from hangman_art.py file
print(logo)
game_is_finished = False
lives = len(stages) - 1

# Select a random from the list file hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a list of underscores to represent the random word
display = []
for _ in range(word_length):
    display += "_"

# Main game loop
while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])