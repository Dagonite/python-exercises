"""
Create a function that returns the majority vote in a list. A majority vote is
an element that occurs > n/2 times in a list (where n is the length of the
list). If the list is empty or there is no majority, return None.
"""


def majority_vote(votes):
    for vote in set(votes):
        n = votes.count(vote)
        if n > len(votes) / 2:
            return vote


if __name__ == "__main__":
    test_cases = [
        ["A", "A", "C"],
        ["B", "B", "C", "D", "B", "A", "B"],
        ["A", "B", "C", "A", "A", "A", "B", "B"],
    ]

    answers = [
        "A",
        "B",
        None,
    ]

    for i, test_case in enumerate(test_cases):
        res = majority_vote(test_case)
        print([answers[i] == res], res)
