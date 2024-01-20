"""
50 ms runtime beats 5.43%
16.49 MB memory beats 28.02%
"""
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l = r = 0
        i = j = 0
        n = len(word1)
        m = len(word2)
        while l < n and r < m:
            if word1[l][i] != word2[r][j]:
                return False
            if i + 1 == len(word1[l]):
                l += 1
                i = 0
            else:
                i += 1
            if j + 1 == len(word2[r]):
                r += 1
                j = 0
            else:
                j += 1
        if l < n or r < m:
            return False
        return True