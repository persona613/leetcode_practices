"""
44 ms runtime beats 23.52%
16.1 MB memory beats 83%
"""
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return 2
            i += 1
            j -= 1
        return 1
        