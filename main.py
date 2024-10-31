import random
import itertools

suits = ["c", "d", "h", "s"]
values = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card:
    def __init__(self, suit, val):
        self.value = val
        self.suit = suit
    def show(self):
        return (self.suit, self.value)

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

def permutate(array):
    return [list(permutation) for permutation in itertools.permutations(array)]

def sort_variations(all_permutation):
    return sorted(all_permutation)[::-1]

def validate(five):
    first = five[0].value
    last = five[-1].value
    middle = [card.value for card in five[1:4]]
    sorted_middle = sort_variations(middle)

    for i in range(len(sorted_middle)):
        if middle == sorted_middle:
            increment = i + 1
            if ((first + increment) % 12 == last) and (five[0].suit == five[-1].suit):
                return True
    return False

def main():
    five_cards = choose_five()
    permutations =  permutate(five_cards)
    for variation in permutations:
        if validate(variation):
            print(f"Deck: {[i.show() for i in variation]}")
            print(f"Ordered four cards (top to bottom){[i.show() for i in variation[:4]]}")
            print(f"Hidden card: {variation[-1].show()}")
            break

if __name__ == "__main__":
    main()