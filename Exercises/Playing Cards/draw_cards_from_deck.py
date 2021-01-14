# draw_cards_from_deck.py
"""Make a standard deck of cards, shuffle the deck, and then draw two cards at random. Print the two cards."""

from random import choice, shuffle

RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
SUITS = ("Diamonds", "Hearts", "Clubs", "Spades")
CARDS = [rank + " of " + suit for rank in RANKS for suit in SUITS]
shuffle(CARDS)

first_card = choice(CARDS)
CARDS.remove(first_card)
print("Your first card is the", first_card)

second_card = choice(CARDS)
CARDS.remove(second_card)
print("\nYour second card is the", second_card)