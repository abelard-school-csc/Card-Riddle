suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
values = [1, 2, 3, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

class Card:
    def __init__(self, suit, val):
        self.value = val
        self.suit = suit

deck = []

for suit in suits:
    for value in values:
        new_card = Card(suit, value)
        deck.append(new_card)

for card in deck:
    print(f"Suit: {card.suit}, Value: {card.value}")
