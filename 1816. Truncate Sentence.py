"""
67 ms runtime beats 5.4%
13.8 MB memory beats 57.50%
"""
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:

        return " ".join(s.split()[:k])