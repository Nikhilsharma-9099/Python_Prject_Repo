from art import logo

print(logo)

bid_dict = {}

name = input("What is your name? ")
bid = int(input("What is your bid? $"))
bid_dict[name] = bid

should_continue = True

while should_continue:
    response = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if response == "yes":
        name = input("What is your name? ")
        bid = int(input("What is your bid? $"))
        bid_dict[name] = bid
    
    else:
        should_continue = False
        
max_bid = max(bid_dict.values())
winners = [name for name, bid in bid_dict.items() if bid == max_bid]

if len(winners) == 1:
    print(f"{winners[0]} is the winner with a bid of ${max_bid}")
else:
    print(f"The winners are {', '.join(winners)} with a bid of ${max_bid}")
        
