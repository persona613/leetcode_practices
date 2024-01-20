"""
630 ms runtime beats 80.29%
16.62 MB memory beats 65.28%
"""
class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1]*10
        for i in range(1, n):
            # next dp
            nxt = [0]*10
            for v in range(10):
                if v == 0:
                    nxt[v] = dp[4]+dp[6]
                elif v == 1:
                    nxt[v] = dp[6]+dp[8]
                elif v == 2:
                    nxt[v] = dp[7]+dp[9]
                elif v == 3:
                    nxt[v] = dp[4]+dp[8]
                elif v == 4:
                    nxt[v] = dp[0]+dp[3]+dp[9]
                elif v == 5:
                    pass
                elif v == 6:
                    nxt[v] = dp[0]+dp[1]+dp[7]
                elif v == 7:
                    nxt[v] = dp[2]+dp[6]
                elif v == 8:
                    nxt[v] = dp[1]+dp[3]
                else:
                    nxt[v] = dp[2]+dp[4]
            dp = nxt
        return sum(dp)%(10**9+7)