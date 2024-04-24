"""
37 ms runtime beats 38.20%
16.54 MB memory beats 26.62%
"""
class Solution:
    def removeVowels(self, s: str) -> str:
        vs = "aeiou"
        res = []
        for i in range(len(s)):
            if s[i] not in vs:
                res.append(s[i])
        return "".join(res)