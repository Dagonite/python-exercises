"""
Make a standard deck of cards, shuffle the deck, and then draw two cards at
random. Print the two cards.
"""

from random import choice, shuffle

RANKS = tuple("2345678910") + ("Jack", "Queen", "King", "Ace")
SUITS = ("Diamonds", "Hearts", "Clubs", "Spades")
cards = [f"{rank} of {suit}" for rank in RANKS for suit in SUITS]
shuffle(cards)

first_card = choice(cards)
cards.remove(first_card)
print("Your first card is the", first_card)

second_card = choice(cards)
cards.remove(second_card)
print("\nYour second card is the", second_card)
