"""
42 ms runtime beats 8.17%
16.2 MB memory beats 36.39%
"""
class Solution:
    def canWinNim(self, n: int) -> bool:
        return True if n % 4 != 0 else False