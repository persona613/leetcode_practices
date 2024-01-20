"""
120 ms runtime beats 95.28%
23.44 MB memory beats 17.14%
"""
class Solution:
    def sortVowels(self, s: str) -> str:
        vos = "aeiouAEIOU"
        arr = []
        pos = []
        for i, c in enumerate(s):
            if c in vos:
                arr.append(c)
                pos.append(i)
        if not arr: return s
        arr.sort()
        s = list(s)
        for p, a in zip(pos, arr):
            s[p] = a
        return "".join(s)
