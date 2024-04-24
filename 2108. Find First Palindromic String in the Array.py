"""
64 ms runtime beats 97.66%
16.79 MB memory beats 59.17%
"""
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""