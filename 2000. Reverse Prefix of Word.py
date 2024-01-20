"""
40 ms runtime beats 43.71%
16.26 MB memory beats 49.74%
"""
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x = word.find(ch)
        if x < 0:
            return word
        return word[:x+1][::-1] + word[x+1:]