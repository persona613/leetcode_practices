"""
43 ms runtime beats 84.97%
14.6 MB memory beats 31.70%
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cs = Counter(s)
        ct = Counter(t)
        return cs == ct