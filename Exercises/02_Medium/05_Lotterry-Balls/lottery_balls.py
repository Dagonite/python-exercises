# lottery_balls.py
"""Script which picks 6 random Lottery balls."""

from random import sample

BALLS = range(1, 60)
chosen_balls = list(map(str, sample(BALLS, 6)))
chosen_balls.sort()

print("Your chosen balls are:", " - ".join(chosen_balls))
