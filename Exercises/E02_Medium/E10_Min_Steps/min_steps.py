"""
Alexa is given n piles of boxes which are of equal or unequal heights. In one 
step, Alexa can remove any number of boxes from the pile which has the maximum 
height and try to make it equal to the one which is just lower than the maximum 
height of the stack. Determine the minimum number of steps required to make all 
of the piles equal in height. For example:

Start:
1 ||||
2 ||
3 ||||||

Step 1:
1 ||||
2 ||
3 ||||

Step 1:
1 ||
2 ||
3 ||||

Step 3:
1 ||
2 ||
3 ||

Total steps: 3
"""


def min_steps(piles):
    total = 0
    desc_piles = sorted(piles, reverse=True)
    for i in range(len(desc_piles) - 1):
        if desc_piles[i] > desc_piles[i + 1]:
            total += i + 1
    return total


if __name__ == "__main__":
    test_cases = [[1, 2, 3], [4, 2, 6], [4, 5, 12, 11], [8, 2, 1, 5, 6, 6]]

    answers = [3, 3, 6, 13]

    for i, test_case in enumerate(test_cases):
        res = min_steps(test_case)
        print("[Pass]" if answers[i] == res else "[Fail]", res)
