"""
36 ms runtime beats 70.58%
16.61 MB memory beats 45.47%
"""
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "1" * (s.count("1") - 1) + "0" * s.count("0") + "1"