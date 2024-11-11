# Card Trick Riddle Coding Project

This project simulates a card trick riddle, where one person keeps a secret card from a randomly drawn set of five. Using a series of prearranged rules, the remaining four cards are handed back in a specific order. The program then identifies the kept card based on agreed-upon logic related to suits, values, and sorting order.

## Overview

The assignment involves:
- Drawing five random cards from a deck.
- Using a predefined set of rules to sort the remaining four cards.
- Identifying the kept card using the sorted order and the difference between the cards' values and suits.

## Project Structure

### Code Description
- **Card Class**: Represents a card with a suit and value, and includes the `show()` method to display a card's suit and value.
- **make_deck**: Generates a deck of 52 cards, including all suits and values.
- **choose_five**: Randomly selects five cards from the deck, which are used for the trick.
- **sort_remaining_cards**: Sorts the remaining three cards by value and suit using a suit hierarchy (spades > hearts > diamonds > clubs).
- **validate**: This function:
  - Identifies two cards with the same suit and determines the difference in their values.
  - Sorts the remaining three cards.
  - Matches the calculated difference with the required order for the remaining cards.
  - Prints the instructions, showing the hidden card and the ordered cards.
- **main**: Orchestrates the program by:
  - Drawing five random cards.
  - Generating all permutations of the five cards.
  - Checking each permutation against the trick’s rules until a valid order is found.
  - Printing the results: the hidden card and the ordered remaining cards.

### Execution
To run the program:
1. Generate a random five-card draw.
2. Check all permutations of these five cards.
3. If a valid permutation is found, display the sorted cards and the hidden card.
4. The program prints instructions showing which card should be kept hidden and how to order the remaining four cards.

### Key Features:
- **Suit Hierarchy**: The program sorts cards by their suit priority: Spades > Hearts > Diamonds > Clubs.
- **Card Pairing and Difference**: The program ensures that the two cards of the same suit provide the necessary information to determine the hidden card.
- **Permutation Validation**: The code validates every possible permutation of the five cards until it finds one that fits the trick’s rules.

## Rules & Logic

1. **Suit Matching**: The first and last card must be of the same suit.
2. **Card Difference**: The difference between the values of the first and last card is used to determine the order of the remaining cards. This difference must be between 1 and 6 (inclusive).
3. **Middle Three Cards**: The middle three cards are sorted in descending order based on their value and suit.

These rules ensure that the hidden card can be accurately determined from the remaining cards.

## Getting Started

To run the project:
1. Ensure Python is installed on your machine.
2. Clone the repository or download the script.
3. Run the script with `python3 main.py`.
4. Follow the prompts to view the results of the card trick.
