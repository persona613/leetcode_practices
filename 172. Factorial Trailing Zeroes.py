"""
69 ms runtime beats 34.49%
16.56 MB memory beats 35.88%
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5
                ans += 1
        return ans