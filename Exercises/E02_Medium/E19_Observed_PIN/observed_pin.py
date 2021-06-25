"""A keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
    
A PIN as been observed as 1357, however it is possible that each of the digits could actually be another adjacent digit
(horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. Giving a PIN as a
string, return a list of all possible variations of the PIN."""

from itertools import product

NEIGHBOURS = {
    "0": ("0", "8"),
    "1": ("1", "2", "4"),
    "2": ("1", "2", "3", "5"),
    "3": ("2", "3", "6"),
    "4": ("1", "4", "5", "7"),
    "5": ("2", "4", "5", "6", "8"),
    "6": ("3", "5", "6", "9"),
    "7": ("4", "7", "8"),
    "8": ("7", "5", "8", "9", "0"),
    "9": ("5", "8", "9"),
}


def get_pins(observed):
    """
    Solution that gets all the possible products using the value of each digit adjacent to the key (including the
    key's digit too).

    Another possible solution is to just have a list of strings of the adjacent digits and use the observed PIN as
    indices for the list.
    """
    return ["".join(digits) for digits in product(*(NEIGHBOURS[digit] for digit in observed))]


if __name__ == "__main__":
    test_cases = [
        "1",
        "22",
        "023",
    ]

    answers = [
        [
            "1",
            "2",
            "4",
        ],
        [
            "11",
            "12",
            "13",
            "15",
            "21",
            "22",
            "23",
            "25",
            "31",
            "32",
            "33",
            "35",
            "51",
            "52",
            "53",
            "55",
        ],
        [
            "012",
            "013",
            "016",
            "022",
            "023",
            "026",
            "032",
            "033",
            "036",
            "052",
            "053",
            "056",
            "812",
            "813",
            "816",
            "822",
            "823",
            "826",
            "832",
            "833",
            "836",
            "852",
            "853",
            "856",
        ],
    ]

    for i, test_case in enumerate(test_cases):
        res = get_pins(test_case)
        print("[PASS]" if answers[i] == res else "[FAIL]", f"get_pins('{test_case}') = {res}")