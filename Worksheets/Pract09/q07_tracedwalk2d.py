# q07_tracedwalk2d.py

from random import random

import numpy as np


def simulate_steps(cols, rows):
    """
    7. [Harder] Write a two-dimensional version tracedwalk2d.py of tracedwalk.py. This should simulate a single random
    walk of the form considered in pract08, where the walker begins in the central square of a square two dimensional
    grid of dimensions 9 by 9 steps, and where the walk ends when the walker steps off the grid. Output the results in
    tabular form. Hint: you may need to use nested (two dimensional) lists.
    """
    grid = [[0] * cols for _ in range(rows)]
    current_col = int(cols / 2)
    current_row = int(rows / 2)

    while True:
        random_step = random()
        if random_step < 0.25:
            current_row -= 1  # go up
        elif random_step >= 0.25 and random_step < 0.5:
            current_col += 1  # go right
        elif random_step >= 0.5 and random_step < 0.75:
            current_row += 1  # go down
        else:
            current_col -= 1  # go left

        if current_row == -1 or current_row == rows or current_col == -1 or current_col == cols:
            break

        grid[current_row][current_col] += 1

    grid = np.array(grid)
    print(grid)


if __name__ == "__main__":
    simulate_steps(9, 9)
