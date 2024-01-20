"""
295 ms runtime beats 51.94%
16.48 MB memory beats 68.47%
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [1] * 5
        nxt = [None] * 5
        # [a,e,i,o,u]
        for i in range(1, n):
            for j in range(5):
                if j == 0:
                    nxt[j] = dp[1] + dp[2] + dp[4]
                elif j == 1:
                    nxt[j] = dp[0] + dp[2]
                elif j == 2:
                    nxt[j] = dp[1] + dp[3]
                elif j == 3:
                    nxt[j] = dp[2]
                else:
                    nxt[j] = dp[2] + dp[3]                
            dp, nxt = nxt, dp
        return sum(dp) % (10**9+7)
        