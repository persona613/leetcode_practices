"""
41 ms runtime beats 32.17%
16.26 MB memory beats 35.39%
"""
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            q = n //2
            ans += q
            if n%2 == 1:
                n = q+1
            else:
                n = q
        return ans
            