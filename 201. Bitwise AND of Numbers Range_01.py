"""
49 ms runtime beats 73.30%
16.45 MB memory beats 98.92%
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1)
        return right