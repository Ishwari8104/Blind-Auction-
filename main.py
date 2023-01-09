from replit import clear
from replit import clear
import art
print(art.logo)
end_of_program=False
total_bids = {}
def finding_highest_bidder(bidding_record):
  highest_bid=0
  for n in bidding_record:
    current_bid = bidding_record[n]
    if current_bid>highest_bid:
      highest_bid=current_bid
      winner = n
  print(f"The winner is {winner} with a bid of {highest_bid}.")
while end_of_program==False:
   name = input("What is your name?")
   bid = int(input("What's your bid?$"))
   total_bids[name]=bid
   decision = input("Are there any other bidders?Type yes or no").lower()
   if decision=="yes":
    clear()
   else:
    end_of_program=True
    finding_highest_bidder(total_bids)
