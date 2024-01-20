"""
108 ms runtime beats 80.85%
17.91 MB memory beats 11.97%
"""
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sd = Counter(s)
        td = Counter(t)
        ans = 0
        for c in td:
            if td[c] > sd[c]:
                ans += td[c] - sd[c]
        return ans