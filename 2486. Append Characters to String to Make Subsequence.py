"""
51 ms runtime beats 88.18%
17.62 MB memory beats 29.07%
"""
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        i = 0
        for c in s:
            if c == t[i]:
                i += 1
                if i >= n:
                    return 0
        return n - i