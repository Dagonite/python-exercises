"""q03_coin.py"""


class Coin:
    """
    3. Create a class called "Coin". The coin will have a value in pence, which
    is passed into the object at creation __init__(value). Using the random
    class, write a method which can simulate flipping the coin, returning either
    heads or tails flip_coin(). You can assume that the coin is fair (i.e.
    50% chance of it landing on heads). Return to pract08 for a reminder of
    using the random module.
    """

    def __init__(self, value):
        self.value = value

    def flip_coin(self):
        from random import random

        return "Heads" if random() < 0.5 else "Tails"


if __name__ == "__main__":
    coin1 = Coin(1)
    print(coin1.flip_coin())
