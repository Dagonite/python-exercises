"""
Given three arrays of the same length containing integers, loop over the arrays
and print the three values at each index. If one index produces the values (1,
2, 2) and a subsequent index produces the values (2, 1, 2); do not print the
latter combination as it contains the same values as the former.
"""

a = [1, 1, 1, 2, 8, 6, 1]
b = [2, 4, 6, 1, 4, 18, 61]
c = [2, 8, 18, 2, 1, 1, 8]

print((" " * 7).join("abc"))

combinations = []
for i, (a_value, b_value, c_value) in enumerate(zip(a, b, c)):
    sorted_combination = sorted((a_value, b_value, c_value))

    if sorted_combination not in combinations:
        combinations.append(sorted_combination)
        print(f"{a_value:<8}{b_value:<8}{c_value}")
