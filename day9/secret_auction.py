from logo import logo
from os import system

def find_higgest(allBids):
    # max = 0
    # winner = ''
    # for bidder in allBids:
    #     if allBids[bidder] > max:
    #         winner = bidder
    #         max = allBids[bidder]
    # print(logo)
    # print(f'The winner is {winner} with a bid of ${max}.')

    print(f'The winner is {max(allBids, key=allBids.get)} with a bid of ${allBids[max(allBids, key=allBids.get)]}.')

over = True
bids = {}
system('clear')

while over:
    print(logo)
    name = input('What is your name: ')
    bid = int(input('What\'s your bid: $'))
    bids[name] = bid
    if input('Are there any other bidders? Type \'yes\' or \'no\': ') == 'no':
        over = False
    system('clear')

find_higgest(allBids=bids)
