"""
36 ms runtime beats 69.73%
16 MB memory beats 100%
"""
class Solution:
    def generateTheString(self, n: int) -> str:
        return "a"*n if n%2 else "a"*(n-1)+"b"