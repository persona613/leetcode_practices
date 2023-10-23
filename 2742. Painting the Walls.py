"""
1924 ms runtime beats 47.78%
53.3 MB memory beats 41.85%
"""
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[None for w in range(n+1)] for i in range(n+1)]

        # kps(ith wall, unpainted wall's nums)
        def kps(cost, time, i, w):
            if w <= 0:
                return 0
            if dp[i][w] != None:
                return dp[i][w]
            if i == 1:
                wp = time[i-1]+1
                if w-wp <= 0:
                    dp[i][w] = cost[0]
                else:
                    dp[i][w] = float("inf")
                return dp[i][w]
            # wall painted
            wp = time[i-1]+1
            pk = cost[i-1]+kps(cost, time, i-1, w-wp)
            npk = kps(cost, time, i-1, w)
            dp[i][w] = min(pk, npk)
            return dp[i][w]

        return kps(cost, time, n, n)