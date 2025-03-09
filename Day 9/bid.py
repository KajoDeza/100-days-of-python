import art

print("Welcome to the online biding")
print(art.logo)

the_name = input("What is your name? ")
the_bid = int(input("What is your bid? $ "))

bids = {}
bids[the_name] = the_bid

should_continue = input("Are there any other bidders? "
                "Type 'yes' if there are others, otherwise type 'no' ").lower()


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of $ {highest_bid}")


bids = {}
continue_biding = True


def find_hightest_bidder(bids):
    pass


while continue_biding:
    the_name = input("What is your name? ")
    the_bid = int(input("What is your bid? $ "))
    bids[the_name] = the_bid
    should_continue = input("Are there any other bidders? Type 'yes' if there are others, otherwise type 'no' ").lower()
    if should_continue == "no":
        continue_biding = False
        find_hightest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)



