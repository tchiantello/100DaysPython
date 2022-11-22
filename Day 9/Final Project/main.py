#from replit import clear
#HINT: You can call clear() to clear the output in the console.
from symbol import continue_stmt
from art import logo

print(logo)

all_bids = {}
winning_bid = 0
winning_person = ""

def add_bid (name, bid):
    all_bids[name] = bid

continue_running = True
while continue_running:
    name = input("What is your name? ")
    bid = int(input("Enter your bid: "))
    add_bid(name, bid)
    another = input("Are there any other people (Y/N)? ").lower()
    if another == "n":
        continue_running = False
        for bid in all_bids:
            if all_bids[bid] > winning_bid:
                winning_bid = all_bids[bid]
                winning_person = bid
        print(f"{winning_person} wins with the bid of: {winning_bid}.")


