"""
Runtime: 2195 ms, faster than 70.20% of Python3 online submissions 
Memory Usage: 16.86 MB, less than 74.60% of Python3 online submissions 
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf] * (n+1)
        # init
        dp[0] = 0
        # i=coins, j=backpack
        for i in range(1, int(n**0.5)+1):
            for j in range(i*i, n+1):
                dp[j] = min(dp[j], dp[j-i*i]+1)
        return dp[-1]
