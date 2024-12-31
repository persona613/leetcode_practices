"""
827 ms runtime beats 33.77%
16.72 MB memory beats 65.24%
"""
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        def is_celebrity(cand):
            for j in range(n):
                if j == cand:
                    continue
                if knows(cand, j) or not knows(j, cand):
                    return -1
            return cand

        # rule out candidates
        cand = 0
        for j in range(n):
            if knows(cand, j):
                cand = j
        return is_celebrity(cand)