"""
662 ms runtime beats 94.48%
17.92 MB memory beats 11.97%
"""
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:

    @lru_cache(None)
    def cache_know(self, a, b):
        return knows(a, b)

    def findCelebrity(self, n: int) -> int:
        # rule out candidate
        ca = 0
        for b in range(1, n):
            if self.cache_know(ca, b):
                ca = b

        for b in range(n):
            if ca == b:
                continue
            if (
                self.cache_know(ca, b) or
                not self.cache_know(b, ca)
                ):
                return -1
        return ca
        