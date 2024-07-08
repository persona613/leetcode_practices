"""
47 ms runtime beats 70.15%
16.55 MB memory beats 93.72%
"""
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1: return words[0]
        chars = set(words[0])
        res = []
        for char in chars:
            freq = min([word.count(char) for word in words])
            res += freq * [char]
        return res
