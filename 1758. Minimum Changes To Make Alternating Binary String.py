"""
51 ms runtime beats 60.50%
17.46 MB memory beats 5.67%
"""
class Solution:
    def minOperations(self, s: str) -> int:
        # str0: s start "0", str1: s start "1"
        str0, str1 = 0, 1
        cost0 = cost1 = 0
        for a in s:
            if int(a) != str0:
                cost0 += 1
            else:
                cost1 += 1
            str0 ^= 1
            str1 ^= 1
        return min(cost0, cost1)