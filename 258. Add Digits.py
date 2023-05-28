"""
35 ms runtime beats 55.47%
13.7 MB memory beats 90.86%
"""
class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1) % 9 + 1 if num else 0