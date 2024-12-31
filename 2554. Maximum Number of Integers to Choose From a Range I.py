"""
41 ms runtime beats 81.14%
18.80 MB memory beats 24.28%
"""
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban = set(banned)
        pick = sm = 0
        for i in range(1, n + 1):
            if i in ban:
                continue
            if sm + i > maxSum:
                break
            sm += i
            pick += 1
        return pick
        