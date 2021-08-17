import random


class Card():
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return self.name + " of " + self.suit

## Welcome and Input for Player
print("Ready Player 1?  What is your name?")
player_1 = input()
print("Good Luck " + player_1 +"!  You are going to need it")
print("Let's Go To War")

## Creates deck
names = [ "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" ]
values = range(1,14)
suits = [ "Clubs", "Diamonds", "Hearts", "Spades" ]
name_values = zip(names, values)
deck = []

for card in name_values:
    for suit in suits:
        deck.append(Card(card[0], suit, card[1]))

new_deck = list(range(1,53))

## Shuffles Deck
shuffled = random.sample(deck, len(deck))
#print (shuffled[0], shuffled[0].value)
##Deals Hands
your_hand = shuffled[::2]
my_hand = shuffled[1::2]
#print(shuffled)
#print(your_hand, len(your_hand))
#print(my_hand, len(my_hand))
while len(my_hand) > 0 or len(your_hand) > 0:
    your_card = your_hand.pop(0)
    my_card = my_hand.pop(0)
    print("You played {}. I played {}.".format(your_hand[0], my_hand[0]))
    if your_hand[0].value > my_hand[0].value:
        your_hand.append(my_card)
        your_hand.append(your_card)
        print("You Won!")
    elif your_hand[0].value < my_hand[0].value:
        my_hand.append(my_card)
        my_hand.append(your_card)
        print("I Won!")
    else:
        print("It's a Tie!  Let's Go To War")
        break
    print("I have {} cards in my deck.  You have {} cards in your deck".format(len(my_hand),len(your_hand)))
if len(my_hand) == 0:
    print ("You Took All Of My Cards.  You Win")
else:
    print ("I Took All Of Your Cards.  I Win")
