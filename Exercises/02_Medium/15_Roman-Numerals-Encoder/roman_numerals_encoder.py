# roman_numerals_encoder.py
"""Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral 
representation of that integer."""


def roman_numerals_encoder(n):
    if n > 3999:
        return None

    ROMAN_NUMERALS = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    roman_string = ""

    for key in sorted(ROMAN_NUMERALS.keys(), reverse=True):
        while n >= key:
            roman_string += ROMAN_NUMERALS[key]
            n -= key

    return roman_string


if __name__ == "__main__":
    test_cases = [
        1,
        4,
        6,
        14,
        21,
        89,
        91,
        984,
        1000,
        1889,
        1989,
    ]

    answers = [
        "I",
        "IV",
        "VI",
        "XIV",
        "XXI",
        "LXXXIX",
        "XCI",
        "CMLXXXIV",
        "M",
        "MDCCCLXXXIX",
        "MCMLXXXIX",
    ]

    for i, test_case in enumerate(test_cases):
        res = roman_numerals_encoder(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", test_case, res)
