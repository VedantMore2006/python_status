def higest_bdder(bidding_records):
    winner = ""
    highest_bid = 0
    for b in bidding_records:
        bit_amount = bidding_records[b]
        if highest_bid < bit_amount:
            highest_bid = bit_amount
            winner = b
    print(f"The winner is {winner} with the bid of ${highest_bid}")


end = "yes"
bidder = {}
while end != "no":
    name = input("Enter your name : ")
    bid = int(input("The amount of money u wnat to bid : "))
    bidder[name] = bid
    end = input("Are there anymore bidder?? 'yes' or 'no'")
    if end == "no":
        higest_bdder(bidder)
