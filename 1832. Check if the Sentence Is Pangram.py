"""
49 ms runtime beats 5.03%
16.26 MB memory beats 43.73%
"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26