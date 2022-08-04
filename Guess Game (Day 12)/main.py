from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_level():
  difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "hard":
    return HARD_LEVEL_TURNS
  else:
    return EASY_LEVEL_TURNS

def check_guess(answer, guess, turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The number was {guess}")
      
def game():
  # Print logo
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'am thinking of a number which is between 1 and 100.")
  
  turns = set_level()
  answer = randint(1, 100)
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_guess(answer, guess, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
    elif guess != answer:
      print("Guess again.")
  
game()