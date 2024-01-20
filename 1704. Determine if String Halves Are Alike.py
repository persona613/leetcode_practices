"""
33 ms runtime beats 94.64%
17.44 MB memory beats 9.07%
"""
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        a = b = 0
        m = len(s)//2
        for c in s[0: m]:
            if c in vowels:
                a += 1
        for c in s[m:]:
            if c in vowels:
                b += 1
        return a == b