"""
60 ms runtime beats 21.44%
16.47 MB memory beats 97.37%
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # find common prefix
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift