"""
39 ms runtime beats 62.89%
16.2 MB memory beats 70.44%
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        n&(n-1)==0, filter in 2**n
        (n-1)%3, filter in 4**n
        """
        return n>0 and n&(n-1)==0 and (n-1)%3==0