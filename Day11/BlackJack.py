import random

def evaluateRETURN(hand):
    acecnt = 0
    count = 0
    for card in hand:
        if(card == "A"):
            acecnt +=1
        elif(isinstance(card,int)):
            count+=card
        elif(card == "K" or card == "Q" or card == "J"):
            count+=10

    while(acecnt != 0):
        if (count <= 10):
            count+= 11
        else:
            count+=1
        acecnt-=1
    return count

def evaluate(hand,name):
    acecnt = 0
    count = 0
    for card in hand:
        if(card == "A"):
            acecnt +=1
        elif(isinstance(card,int)):
            count+=card
        elif(card == "K" or card == "Q" or card == "J"):
            count+=10

    while(acecnt != 0):
        if (count <= 10):
            count+= 11
        else:
            count+=1
        acecnt-=1
    print(f"Hand of {name} is : {count}")
    


def hit(hand):
    card = random.randint(0,12)
    hand.append(deck[card])

deck = ["A",2,3,4,5,6,7,8,9,10,"Q","J","K"]
dealer = []
player = []


hit(player)
hit(player)

print(f"Player hand is {player}")
evaluate(player,"Player")

hit(dealer)
hit(dealer)
print(f"Dealers hand is {dealer[0]} and a hidden card")

loop = input("Hit or Stand(h to hit and s to stand)")
while(loop == "h"):
    hit(player)
    print(f"Current hand is {player}")
    evaluate(player,"Player")
    loop = input("Hit or Stand(h to hit and s to stand)")

print(f"Dealer Reveals hand... {dealer}")
loop = True
while(loop):
    if ((evaluateRETURN(dealer) < evaluateRETURN(player)) and (evaluateRETURN(player) <=21) ):
        hit(dealer)
        print(f"Dealer hits, Dealers hand ... {dealer}")
    else:
        print(f"Dealer stands... {dealer}")
        loop = False

print("Determining Winner...")
if((evaluateRETURN(dealer) > evaluateRETURN(player) and evaluateRETURN(dealer)<=21) or (evaluateRETURN(dealer)<=21 and evaluateRETURN(player)>21)):
    print("Dealer Wins  :/  ")
elif(((evaluateRETURN(player) > evaluateRETURN(dealer)) and evaluateRETURN(player)<=21) or (evaluateRETURN(player)<=21 and evaluateRETURN(dealer)>21)):
    print("Player Wins  :D")
else:
    print("No one Wins, DRAW...")