"""Script which picks 6 random Lottery balls."""

from random import sample

BALLS = range(1, 60)
chosen_balls = sample(BALLS, 6)
chosen_balls.sort()

print(*chosen_balls, sep=" - ")


EM = range(1, 51)
LS = range(1, 13)
chosen_EM = sample(EM, 5)
chosen_LS = sample(LS, 2)

print(chosen_EM)
print(chosen_LS)
