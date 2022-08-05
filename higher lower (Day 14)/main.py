from replit import clear
from art import logo, vs
from game_data import data
import random

def get_random_account():
  return random.choice(data)

def higher_lower(first, second):
  if first['follower_count'] == second['follower_count']:
    return 'A'
  elif first['follower_count'] > second['follower_count']:
    return 'A'
  else:
    return 'B'

def game():
  continue_game = True
  score = 0
  print(logo)
  option_A = get_random_account()
  
  while continue_game: 
    print(f"Compare A: {option_A['name']}, {option_A['description']} from {option_A['country']}")
    print(vs)
    option_B = get_random_account()
    if data.index(option_B) == data.index(option_A):
      option_B = get_random_account()
    
    print(f"Against B: {option_B['name']}, {option_B['description']} from {option_B['country']}")
    higher = higher_lower(option_A, option_B)
    
    user_choice = input("Who has more followers: Type 'A' or 'B': ").upper()
    if user_choice == 'A':
      new_option = option_A
    else:
      new_option = option_B

    clear()
    print(logo)
    if user_choice == higher:
      score += 1
      option_A = new_option
      print(f"You're right! Current score: {score}.")
    else:  
      print(f"sorry that's wrong. Final score: {score}")
      continue_game = False
      
game()