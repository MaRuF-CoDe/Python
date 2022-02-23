import os
clear = lambda: os.system('cls')

from art import logo
print(logo)

# auction = []


# def add(name,price):
#     auc={}
#     auc["Name"] = name
#     auc["Price"]= price
#     auction.append(auc)

# name = input("Enter Your name : ")
# price = int(input("Enter Bid : $"))

# add(name,price)
# end_of_bid = False
# while not end_of_bid:
#     more=input("Is there more people who want to bid ? If yes then type yes or type no").lower()
#     clear()
#     if more == "yes":
#         name = input("Enter Your name : ")
#         price = int(input("Enter Bid : $"))
#         add(name,price)
#     else:
#         end_of_bid = True
   
# for index in range(len(auction)):
#     for key in auction[index]:
#         print(auction[index][key])


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  
