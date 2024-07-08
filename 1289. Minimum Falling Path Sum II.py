"""
221 ms runtime beats 84.58%
20.14 MB memory beats 34.80%
"""
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = grid[0][:]
        # base-dp-row minin, second minin and positions
        ip1 = ip2 = -1
        mi1 = mi2 = inf
        for j in range(n):
            a = dp[j]
            if a < mi1:
                mi2, mi1 = mi1, a
                ip2, ip1 = ip1, j
            elif a < mi2:
                mi2, ip2 = a, j

        for i in range(1, n):
            # curr-dp-row minin, second minin and positions
            cip1 = cip2 = -1
            cmi1 = cmi2 = inf
            for j in range(n):
                if ip1 != j:
                    dp[j] = grid[i][j] + mi1
                else:
                    dp[j] = grid[i][j] + mi2

                if dp[j] < cmi1:
                    cmi2, cmi1 = cmi1, dp[j]
                    cip2, cip1 = cip1, j
                elif dp[j] < cmi2:
                    cmi2 = dp[j]
                    cip2 = j
            mi1, mi2, ip1, ip2 = cmi1, cmi2, cip1, cip2
        return mi1