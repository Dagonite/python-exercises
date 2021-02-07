# majority_vote.py
"""Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in 
a list (where N is the length of the list). If the list is empty or there is no majority, return None."""


def majority_vote(votes):
    for vote in set(votes):
        n = votes.count(vote)
        if n > len(votes) / 2:
            return vote


print(majority_vote(["A", "A", "C"]))
print(majority_vote(["B", "B", "C", "D", "B", "A", "B"]))
print(majority_vote(["A", "B", "C", "A", "A", "A", "B", "B"]))