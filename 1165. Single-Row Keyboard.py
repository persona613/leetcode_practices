"""
52 ms runtime beats 45.20%
17.44 MB memory beats 16.86%
"""
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = dict()
        for i, k in enumerate(keyboard):
            d[k] = i
        ans = d[word[0]]
        for i in range(1, len(word)):
            ans += abs(d[word[i]] - d[word[i-1]])
        return ans