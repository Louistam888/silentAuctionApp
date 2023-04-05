import os 
import logo 

from logo import logo 

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

biddingOpen = True
allBids = []

while biddingOpen == True: 

  print(logo)

  name = input("Enter the bidder's name: ")
  bid = int(input("Enter a bid: $"))

  newBid = {
     "name": name,
     "bid": bid
  }
  
  allBids.append(newBid)

  stillBidding = input("Do you want to continue bidding? Enter 'yes' to continue or 'no' to see who is the winner ")

  if stillBidding == "yes":
    clear_screen()
  elif stillBidding == "no":
    biddingOpen = False
  
    topBid = 0
    topBidder = []
        
for i in allBids:

  if i["bid"] > topBid:
    topBid = i["bid"]
    newTopBidder = {
      "name": i["name"],
      "bid": i["bid"]
    }
    topBidder.append(newTopBidder)
  elif i["bid"] == topBid:
    newTopBidder = {
      "name": i["name"],
      "bid": i["bid"]
    }
    topBidder.append(newTopBidder)

if len(topBidder) == 1:
  print (f'\n AND THE WINNER IS: {topBidder[0]["name"]} with a bid of ${topBidder[0]["bid"]}')
elif len(topBidder) > 1:
  print (f"\n We have a tie! The following bids are all tied for the top bid of ${topBid}: \n")

  for k in range(0, len(topBidder)):
    print(f"{topBidder[k]['name']}")