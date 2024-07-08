"""
61 ms runtime beats 78.26%
17.54 MB memory beats 50.72%
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = Counter(s)
        ans = 0
        for k in d:
            t = d[k]
            ans += t * (t + 1) // 2
        return ans