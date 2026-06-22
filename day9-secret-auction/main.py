# import ASCII art from another file
from art import logo

#print the logo and show a welcome greeting
print(logo)
print("Welcome to the Bid Auction!")

#the bid dictionary
bid_log = {
}
# keep the while loop running while is true
keep_bidding = True
# A loop in case there are more people bidding
while keep_bidding:
    name = input("What's your name? \n")
    bid = int(input("What's the bid? \n"))
    # I can add the name and the bid inputs in the dictionary:
    bid_log[name] = bid

    print("\n" * 20)

    decision = input("Are there other bidders? type 'y' for yes and 'n' for no  \n").lower()
    if decision == "y":
        print("\n" * 20)
    elif decision == "n":
        keep_bidding = False
    else:
        print("Invalid Input, The auction will be stopped")
        keep_bidding = False
# 2 variables to hold the highest bid and the name of the bidder
highest_bid = 0
highest_bidder = ""

# A loop in the dictionary to find the highest bid
for bidder_name, bid_amount in bid_log.items():
    if bid_amount > highest_bid:
        highest_bidder = bidder_name
        highest_bid = bid_amount

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")





