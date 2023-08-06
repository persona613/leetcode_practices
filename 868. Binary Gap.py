"""
53 ms runtime beats 16.5%
16.4 MB memory beats 29.1%
"""
class Solution:
    def binaryGap(self, n: int) -> int:
        bs = bin(n)[2:]
        k = bs.find("1")
        ans = 0
        for i in range(k+1, len(bs)):
            if bs[i] == "1":
                ans = max(ans, i-k)
                k = i
        return ans