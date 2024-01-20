"""
41 ms runtime beats 30.47%
16.2 MB memory beats 34.48%
"""
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        st = sentence.split()
        l = len(searchWord)
        for i in range(len(st)):
            if st[i][:l] == searchWord:
                return i+1
        return -1                