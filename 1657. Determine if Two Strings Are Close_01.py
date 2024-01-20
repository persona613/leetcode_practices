"""
124 ms runtime beats 87.39%
18.52 MB memory beats 5.69%
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1 = Counter(word1)
        d2 = Counter(word2)
        if d1.keys() != d2.keys():
            return False
        a1 = sorted(d1.values())
        a2 = sorted(d2.values())
        return a1 == a2