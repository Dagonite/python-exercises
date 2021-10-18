"""
The median is the middle value in an ordered integer list. If the size of the
list is even, there is no middle value and the median is the mean of the two
middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
•MedianFinder() initializes the MedianFinder object.
•add_Num(num) adds the integer num from the data stream to the data structure.
•double find_median() returns the median of all elements so far.
"""

from heapq import heappush, heappushpop


class MedianFinder:
    """
    Solution using two heaps (or priority queues):

    •Max-heap small has the smaller half of the numbers.
    •Min-heap large has the larger half of the numbers.

    This gives direct access to the one or two middle values (they're the tops
    of the heaps), so getting the median takes O(1) time. And adding a number
    takes O(log n) time.
    """

    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def add_num(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def find_median(self):
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return float(self.large[0] - self.small[0]) / 2.0


if __name__ == "__main__":
    sequence = MedianFinder()
    sequence.add_num(1)
    sequence.add_num(2)
    sequence.add_num(11)
    print(sequence.find_median())
    sequence.add_num(4)
    sequence.add_num(5)
    sequence.add_num(7)
    sequence.add_num(3)
    print(sequence.find_median())
