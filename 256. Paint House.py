"""
52 ms runtime beats 86.37%
16.96 MB memory beats 11.97%
"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        @lru_cache(None)
        def dp(i, j):
            if i < 0:
                return 0            
            return costs[i][j] + min(dp(i - 1, (j + 1) % 3),
                                     dp(i - 1, (j + 2) % 3))
                                     
        i = len(costs) - 1
        return min(dp(i, 0), dp(i, 1), dp(i, 2))