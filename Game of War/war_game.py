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
print (shuffled[0], shuffled[0].value)
##Deals Hands
your_hand = shuffled[::2]
my_hand = shuffled[1::2]
#print(shuffled)
#print(your_hand, len(your_hand))
#print(my_hand, len(my_hand))


