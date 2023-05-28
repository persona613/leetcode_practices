"""
48 ms runtime beats 16.68%
16.3 MB memory beats 17.76%
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word.istitle():
            return True
        return False