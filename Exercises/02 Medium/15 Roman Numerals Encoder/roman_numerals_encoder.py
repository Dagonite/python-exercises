# roman_numerals_encoder.py
"""Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral 
representation of that integer."""


def roman_numerals_encoder(n):
    if n > 3999:
        return None

    SYMBOLS = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    line = ""

    for symbol in reversed(SYMBOLS):
        symbol_value = SYMBOLS[symbol]
        quotient = n // symbol_value
        no_of_symbol = min(3, quotient)
        line += symbol * no_of_symbol
        n -= no_of_symbol * symbol_value

    return line


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
