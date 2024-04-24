"""
60 ms runtime beats 71.27%
17.60 MB memory beats 79.56%
"""
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                j += 1
            i += 1
        return n - j