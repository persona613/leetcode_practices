"""
41 ms runtime beats 48.88%
16.22 MB memory beats 40.24%
"""
class Solution:
    def totalMoney(self, n: int) -> int:
        base = 28
        w = n // 7
        r = n % 7
        ans = 0
        for i in range(1, w+1):
            ans += base
            base += 7
        for i in range(w+1, w+1+r):
            ans += i
        return ans
