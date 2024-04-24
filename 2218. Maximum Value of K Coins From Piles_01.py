"""
Memory Limit Exceeded
108 / 123 testcases passed
Last Executed Input
Use Testcase
piles =

k =
1443
"""
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:        
        # j=top of pile[i], t=k
        @cache
        def dfs(i, j, t):
            if i >= n or t == 0:
                return 0

            # not take curr j := top of pile[i]
            notake = dfs(i + 1, 0, t)
            if j < len(piles[i]):
                # take curr j
                take = piles[i][j] + dfs(i, j + 1, t - 1)
                return max(notake, take)
            else:
                return notake
                
        n = len(piles)
        return dfs(0, 0, k)