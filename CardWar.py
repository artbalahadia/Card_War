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


# Player Class
class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        # Returns the top card in Player's hands
        return self.all_cards.pop()

    def add_card(self, new_cards):
        # If adding multiple cards
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # If adding single cards
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        if len(self.all_cards) <= 1:
            return f'Player {self.name} has {(len(self.all_cards))} card'
        else:
            return f'Player {self.name} has {(len(self.all_cards))} cards'

# New player test
player_1 = Player('Art')
print(player_1)
# Add single card
#player_1.add(jack_diamonds)
#print(player_1)
# Add multiple cards
player_1.add_card([jack_diamonds, two_hearts])
print(player_1)


# START GAME
player_one = Player('Player One')
player_two = Player('Player Two')

game_deck = Deck()
game_deck.shuffle()

# Give cards to each player
for x in range(26):
    player_one.add_card(game_deck.deal_one())
    player_two.add_card(game_deck.deal_one())

game_on = True

round_num = 0

while game_on:
    round_num+=1

    print(f'Round {round_num} begins!')

    if len(player_one.all_cards) == 0:
        print('Player 1 is out of cards. Player 2 Wins!')
        game_on = False

    if len(player_two.all_cards) == 0:
        print('Player 2 is out of cards. Player 1 Wins!')
        game_on = False

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < 5:
                print('Player 1 insufficient cards, War Over. Player 2 Wins!')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player 2 insufficient cards. Player 1 Wins!')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())