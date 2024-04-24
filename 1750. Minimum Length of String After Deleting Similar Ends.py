"""
69 ms runtime beats 60.66%
17.28 MB memory beats 92.89%
"""

class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                break
            if i + 1 == j:
                return 0
            c = s[i]
            while s[i] == c and i < j:
                i += 1
                if i == j:
                    return 0
            while s[j] == c and i < j:
                j -= 1
        
        return j - i + 1