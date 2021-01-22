# draw_cards_using_a_set.py
"""Make a standard deck of cards and draw two cards at random. Print the two cards."""

RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
SUITS = ("Diamonds", "Hearts", "Clubs", "Spades")
cards = {rank + " of " + suit for rank in RANKS for suit in SUITS}

card_one = cards.pop()
print(card_one)

card_two = cards.pop()
print(card_two)