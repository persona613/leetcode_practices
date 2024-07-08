"""
2536 ms runtime beats 57.56%
57.92 MB memory beats 49.27%
"""
class Solution:
    def checkRecord(self, n: int) -> int:
        # 1-index, c=A0:L1:P2, i=index, t=have A:bool
        dp = [[[0] * 2 for i in range(n + 1)] for c in range(3)]

        # init
        # (P,0,False) = 1 for calculation
        dp[2][0][0] = 1

        # (A,1,True), (L,1,False), (P,1,False) = 1
        dp[0][1][1], dp[1][1][0], dp[2][1][0] = 1, 1, 1

        mod = 10 ** 9 + 7
        for i in range(2, n + 1):
            for c in range(3):
                # A
                if c == 0:
                    # (L,False), (P,False) + currA
                    dp[c][i][1] = (dp[1][i-1][0] + dp[2][i-1][0]) % mod
                # L
                elif c == 1:
                    # one-L + two-L
                    # (P,False), (PL,False) + currL
                    dp[c][i][0] = (dp[2][i-1][0] + dp[2][i-2][0]) % mod

                    # one-L + two-L
                    # (A,True), (P,True), (AL,True), (PL,True) + currL
                    dp[c][i][1] = (dp[0][i-1][1] + dp[2][i-1][1] \
                                + dp[0][i-2][1] + dp[2][i-2][1]) % mod
                # P
                else:
                    # (L,False), (P,False) + currP
                    dp[c][i][0] = (dp[1][i-1][0] + dp[2][i-1][0]) % mod

                    # (A,True), (L,True), (P,True) + currP
                    dp[c][i][1] = (dp[0][i-1][1] + dp[1][i-1][1] \
                                + dp[2][i-1][1]) % mod
        ans = 0
        for c in range(3):
            for t in range(2):
                ans += dp[c][n][t] % mod
        return ans % mod