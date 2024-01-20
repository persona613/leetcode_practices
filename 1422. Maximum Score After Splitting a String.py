"""
38 ms runtime beats 82.06%
17.49 MB memory beats 5.69%
"""
class Solution:
    def maxScore(self, s: str) -> int:
        # Zero_left + (One_total - One_left)
        zeros = ones = 0
        best = -inf
        for i in range(len(s)-1):
            if s[i] == "0":
                zeros += 1
            else:
                ones += 1
            best = max(best, zeros - ones)
        if s[-1] == "1":
            ones += 1
        return best + ones
