import random

suits = ["c", "d", "h", "s"]
values = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card:
    def __init__(self, suit, val):
        self.value = val
        self.suit = suit
    def show_card(self):
        print(self.suit, self.value)

deck = []

for suit in suits:
    for value in values:
        new_card = Card(suit, value)
        deck.append(new_card)

chosen_cards = []

for card in range(5):
    card = random.choice(deck)
    deck.remove(card)
    chosen_cards.append(card)

for i in range(len(chosen_cards)):
    for j in range(i + 1, len(chosen_cards)):
        # print(f"First card: {chosen_cards[i].suit}, {chosen_cards[i].value}, Second Card: {chosen_cards[j].suit}, {chosen_cards[j].value}")

        first_suit = chosen_cards[i].suit
        second_suit = chosen_cards[j].suit

        if first_suit == second_suit:
            same_suit = (chosen_cards[i], chosen_cards[j])

print("Same suit:")

for i in same_suit:
    i.show_card()

removed_card = same_suit[0]

remaining_cards = [same_suit[1]]

for i in chosen_cards:
    if i not in same_suit:
        remaining_cards.append(i)

print("Remaning cards:")
for i in remaining_cards:
    i.show_card()
