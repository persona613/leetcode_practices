"""
296 ms runtime beats 11.22%
18.55 MB memory beats 14.44%
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        # bitwise operation
        wordbit1 = wordbit2 = 0
        wf1 = [0] * 26 # word frequency
        wf2 = [0] * 26

        for c in word1:
            d = ord(c) - ord("a")
            wordbit1 = wordbit1 | 1 << d
            wf1[d] += 1
        for c in word2:
            d = ord(c) - ord("a")
            wordbit2 = wordbit2 | 1 << d
            wf2[d] += 1

        if wordbit1 != wordbit2:
            return False        
        return sorted(wf1) == sorted(wf2)