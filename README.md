# Card Trick Riddle Coding Project

This project simulates a card trick riddle, where one person keeps a secret card from a randomly drawn set of five. Using a series of prearranged rules, the remaining four cards are handed back in a specific order. The program then identifies the kept card using the agreed rule.

## Overview

The assignment involves:
- Drawing five cards randomly from a deck.
- Sorting four of these cards to convey information about the hidden card.
- Using code logic to identify the hidden card based on rules about the suits, values, and sorting order.

## Project Structure

### Code Description
- **Card Class**: Represents a card with a suit and value, using `show()` to reveal the card.
- **make_deck**: Builds a deck with 52 cards.
- **choose_five**: Randomly selects five cards from the deck, representing the set for the trick.
- **permutate**: Generates all possible orderings of a list of cards.
- **sort_variations**: Sorts permutations in descending order, setting a structure for comparing potential solutions.
- **validate**: Checks if the ordering of a permutation meets the riddle’s criteria:
  - Matches the three middle cards to a sorted pattern.
  - Ensures consistent suits and a specified increment rule.
- **main**: Runs the program to:
  - Draw and permutate five cards.
  - Validate each permutation until it matches the trick’s rule.
  - Display the sorted four cards and the hidden card.

### Execution
The main script is executed to:
1. Generate a random five-card draw.
2. Evaluate each permutation of these cards.
3. Print the ordered four cards and reveal the hidden card.

## Rules & Logic

1. The values of the middle three cards follow a sorted structure.
2. The first and last card values differ by a specific increment.
3. The suit of the first and last card must match.

These rules ensure that the code can identify the hidden card accurately.

## Getting Started
To run the project:
1. Ensure you have Python installed.
2. Run the script with `python3 main.py`.
3. Follow prompts to view the results of the card trick.

## Contributing
Suggestions for improvements or alternative rules are welcome!