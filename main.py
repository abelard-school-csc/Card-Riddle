# Fixed code with the help of Mr. Brandy's code (used as reference for est validation)
import random
import itertools

suits = ["c", "d", "h", "s"]
values = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]

suit_hierarchy = {'s': 4, 'h': 3, 'd': 2, 'c': 1}

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
    chosen_cards = random.sample(deck, 5)
    return chosen_cards

def sort_remaining_cards(remaining_cards):
    return sorted(remaining_cards, key=lambda x: (x.value, suit_hierarchy[x.suit])) # fancy lambda func

def validate(permutation):
    suit_counts = {}
    for card in permutation:
        if card.suit in suit_counts:
            suit_counts[card.suit].append(card)
        else:
            suit_counts[card.suit] = [card]

    chosen_suit = None
    for suit, cards in suit_counts.items():
        if len(cards) >= 2:
            chosen_suit = suit
            break

    if not chosen_suit:
        return False

    chosen_cards = sorted(suit_counts[chosen_suit], key=lambda x: x.value)
    value1, value2 = chosen_cards[:2]

    raw_difference = (value2.value - value1.value) % 13
    if raw_difference > 6:
        reference_card, hidden_card = value2, value1
        difference = 13 - raw_difference
    else:
        reference_card, hidden_card = value1, value2
        difference = raw_difference if raw_difference != 0 else 1

    remaining_cards = [card for card in permutation if card != reference_card and card != hidden_card]
    remaining_cards_sorted = sort_remaining_cards(remaining_cards)

    ordering_map = {
        1: [remaining_cards_sorted[2], remaining_cards_sorted[1], remaining_cards_sorted[0]],
        2: [remaining_cards_sorted[2], remaining_cards_sorted[0], remaining_cards_sorted[1]],
        3: [remaining_cards_sorted[1], remaining_cards_sorted[2], remaining_cards_sorted[0]],
        4: [remaining_cards_sorted[1], remaining_cards_sorted[0], remaining_cards_sorted[2]],
        5: [remaining_cards_sorted[0], remaining_cards_sorted[2], remaining_cards_sorted[1]],
        6: [remaining_cards_sorted[0], remaining_cards_sorted[1], remaining_cards_sorted[2]],
    }

    encoded_order = ordering_map[difference]

    print("\nInstructions:")
    print(f"Keep this card hidden: ({hidden_card.suit}, {hidden_card.value})")
    print("Order the remaining four cards as follows:")
    print(f"  - ({reference_card.suit}, {reference_card.value})")
    for card in encoded_order:
        print(f"  - ({card.suit}, {card.value})")

    return True

def main():
    five_cards = choose_five()
    print("Chosen cards: ", [card.show() for card in five_cards])
    
    permutations = list(itertools.permutations(five_cards))
    for permutation in permutations:
        if validate(permutation):
            break

if __name__ == "__main__":
    main()
