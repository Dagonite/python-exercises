"""
Write a function, which takes a non-negative integer (seconds) as input and 
returns the time in a human-readable format (HH:MM:SS).

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59).
"""


def make_readable(seconds):
    hh = seconds // 3600
    mm = seconds // 60 % 60
    ss = seconds % 60
    return "{:02}:{:02}:{:02}".format(hh, mm, ss)


if __name__ == "__main__":
    test_cases = [
        8,
        60,
        68,
        3781,
        23908,
    ]

    answers = [
        "00:00:08",
        "00:01:00",
        "00:01:08",
        "01:03:01",
        "06:38:28",
    ]

    for i, test_case in enumerate(test_cases):
        res = make_readable(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
