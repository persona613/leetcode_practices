"""
43 ms runtime beats 97.59%
16.70 MB memory beats 62.60%
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = [0] * 26
        base = ord("a")
        for c in s1:
            freq[ord(c) - base] += 1
        
        ln = len(s1)
        window = [0] * 26
        for i in range(ln - 1):
            window[ord(s2[i]) - base] += 1

        for i in range(ln - 1, len(s2)):
            window[ord(s2[i]) - base] += 1
            if window == freq:
                return True
            window[ord(s2[i - ln + 1]) - base] -= 1
        return False
        