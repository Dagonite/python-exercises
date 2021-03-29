# print_array_elements.py
"""Give three arrays (a, b, and c) of the same length, containing integers. Loop over the arrays and print their 
contents. For these numbers the order they are in across the arrays does not matter, so (1, 2, 2) == (2, 2, 1). Do not
print duplicates."""

a = [1, 1, 1, 2, 8, 6, 1]
b = [2, 4, 6, 1, 4, 18, 61]
c = [2, 8, 18, 2, 1, 1, 8]

print("a      b      c")
combinations = []

for i in range(len(min(a, b, c))):
    sorted_combination = sorted((a[i], b[i], c[i]))

    if sorted_combination in combinations:
        continue  # ignore combination if it is already in combinations

    combinations.append(sorted_combination)
    print(f"{a[i]:<7}{b[i]:<7}{c[i]}")
