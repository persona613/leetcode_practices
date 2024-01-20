"""
72 ms runtime beats 9.27%
17.49 MB memory beats 5.61%
"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = dict()
        ans = -inf
        for i in range(len(s)):
            if s[i] in d:
                ans = max(ans, i - d[s[i]] - 1)
                d[s[i]] = min(d[s[i]], i)
            else:
                d[s[i]] = i
        return -1 if ans == -inf else ans