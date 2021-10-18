"""
Given a pattern followed by text blobs split by "|". Create a function which
returns a string showing the number of times the pattern is present in each blob
and the total number of matches at the end.

Input:
"cc;cc|ccc|cac|ccacc|ccbaccc"

Where "cc" is the pattern.
And "cc", "ccc", "cac", "ccacc", and "ccbaccc" are the text blobs.

Output:
"1|2|0|2|3|8"
"""


def count_occurrences(blob, pattern):
    occurences = 0
    index = 0
    while True:
        position = blob.find(pattern, index)
        if position < 0:
            break
        occurences += 1
        index = position + 1
    return occurences


def recognise_patterns(line):
    split_input = line.split(";")
    pattern, blobs = split_input[0], split_input[1].split("|")

    output_str = ""
    total = 0
    if pattern == "":
        output_str = "0|" * len(blobs)
    else:
        for blob in blobs:
            occurences = count_occurrences(blob, pattern)
            output_str += str(occurences) + "|"
            total += occurences
    output_str += str(total)
    return output_str


if __name__ == "__main__":
    test_cases = [
        ";bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32",
        "aa;aaaakjlhaa|aaadsaaa|easaaad|sa",
        "b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32",
        "bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32",
        "cc;cc|ccc|cac|ccacc|ccbaccc",
    ]

    answers = [
        "0|0|0|0|0",
        "4|4|2|0|10",
        "4|2|3|2|11",
        "3|2|1|2|8",
        "1|2|0|2|3|8",
    ]

    for i, test_case in enumerate(test_cases):
        res = recognise_patterns(test_case)
        print([answers[i] == res], res)
