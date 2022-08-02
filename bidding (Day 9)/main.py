Skip to content



digvijaychouhan
digvijaychouhan
/
blind-auction-start
Python


Run

Publish

Invite













CPU
RAM
Storage

Selection deleted
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
▼
▼
▼
▼
▼
from replit import clear
from art import logo

print(logo)
bids = {}
bidding_finished = False
highest = 0
winner = ""

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   for bidder in bidding_record:
#     bid_amount = int(bidding_record[bidder])
#   if bid_amount > highest_bid:
#     highest_bid = bid_amount
#     winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")
    
while not bidding_finished:
  print("Welcome to the secret auction program.")
  name = input("What is your name?: ").lower()
  price = input("What's your bid? $")
  bids[name] = price
    
  choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if choice == "no":
    bidding_finished = True
    # find_highest_bidder(bids)
    for bidder in bids:
      val = int(bids[bidder])
      if val > highest:
        highest = val
        winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}")
  elif choice == "yes":
    clear()
  
print(bids)


Console

Shell


Enable "Accessible Terminal" in Workspace Settings to use a screen reader with the console.
Downloading files 100%Ready
blind-auction-start - Replit