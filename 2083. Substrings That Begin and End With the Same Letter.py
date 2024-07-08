"""
87 ms runtime beats 38.02%
17.22 MB memory beats 90.91%
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = [0] * 26
        ans = 0
        for ch in s:
            code = ord(ch) - ord("a")
            d[code] += 1
            ans += d[code]
        return ans