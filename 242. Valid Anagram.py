"""
40 ms runtime beats 96.91%
16.95 MB memory beats 32.14%
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)