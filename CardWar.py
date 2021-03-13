# Card Class
#   - Suit (Spade, Heart, Club, Diamond)
#   - Rank (ranks cards from two to fourteen)
#   - Value (translates string numbers to integers)

import random

# Global Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
          'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,
           'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# Individual Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# Cards must be in (value)_(suit) format
two_hearts = Card("Hearts", "Two")
print(two_hearts)
print(two_hearts.value)

jack_diamonds = Card("Diamonds", "Jack")
print(jack_diamonds)
print(jack_diamonds.value)



# Entire Deck Class
class Deck():
    def __init__(self):
        # Empty list of cards
        self.all_cards =  []

        for suit in suits:
            for rank in ranks:
                # Create card object for each suit and rank
                created_card = Card(suit, rank)
                # Insert each card in the deck
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# New deck test
new_deck = Deck()
new_deck.shuffle()
first_draw = new_deck.deal_one()
print(first_draw)