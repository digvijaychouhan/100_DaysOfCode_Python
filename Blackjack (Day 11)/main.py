import art
import replit
import random

def deal_card():
  """ Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
  return random.choice(cards)
    
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 in cards and len(cards) == 2:
    return 0  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You lose 😤"
  elif user_score ==  computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "You lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "You win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over, You lose 😭"
  elif computer_score > 21:
    return "Opponent went over, You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


game_over = False
while not game_over:
  replit.clear()
  user_cards = []
  computer_cards = []
  is_game_over = False
  print(art.logo)
  
  # Deal two cards to each player at the start of game.
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards},   Current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}\n")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_choice = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_choice == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"  Your final hands: {user_cards},   final score: {user_score}")
  print(f"  Computer's final hands: {computer_cards},   final score: {computer_score}\n")
  print(compare(user_score, computer_score))

  game_choice = input(f"Do you want to play Blackjack: Type 'y' or 'n':  ").lower()
  if game_choice == "n":
    game_over = True


  