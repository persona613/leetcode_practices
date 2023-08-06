"""
139 ms runtime beats 90.95%
17 MB memory beats 32.28%
"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        b = s[0]
        n0, n1 = 0, 0
        for c in s:
            if c == b:
                n1 += 1
            else:
                ans += min(n0, n1)
                n0, n1 = n1, 1
                b = c
        return ans + min(n0, n1)

