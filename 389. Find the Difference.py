"""
41 ms runtime beats 60.95%
16.3 MB memory beats 43.9%
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sm = tm = 0
        for c in s:
            sm += ord(c)
        for c in t:
            tm += ord(c)
        return chr(tm-sm)