import random

suits = ["c", "d", "h", "s"]
values = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card:
    def __init__(self, suit, val):
        self.value = val
        self.suit = suit
    def show(self):
        print(self.suit, self.value)

def make_deck():
    deck = []

    for suit in suits:
        for value in values:
            new_card = Card(suit, value)
            deck.append(new_card)

    return deck

def choose_five():
    deck = make_deck()
    chosen_cards = []

    for card in range(5):
        card = random.choice(deck)
        deck.remove(card)
        chosen_cards.append(card)

    return chosen_cards


for i in range(5):
    five_cards = choose_five()