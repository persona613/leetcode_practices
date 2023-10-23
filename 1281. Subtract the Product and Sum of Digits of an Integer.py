"""
45 ms runtime beats 28.82%
16.2 MB memory beats 86.74%
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while n:
            d = n % 10
            p *= d
            s += d
            n //= 10
        return p - s


        # lst = [int(d) for d in str(n)]
        # p = 1
        # for d in lst:
        #     p *= d 
        # return p - sum(lst)