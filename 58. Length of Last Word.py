"""
28 ms runtime beats 91.57%
16.70 MB memory beats 6.34%
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
                