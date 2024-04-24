"""
3729 ms runtime beats 83.07%
246.53 MB memory beats 40.74%
"""
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:        
        @cache
        def dfs(i, remain):
            if i >= n or remain == 0:
                return 0

            # skp curr pile[i]
            ans = dfs(i + 1, remain)
            curr = 0
            # take coins
            for j in range(min(len(piles[i]), remain)):
                curr += piles[i][j]
                ans = max(ans, curr + dfs(i + 1, remain - j - 1))
            return ans

        n = len(piles)
        return dfs(0, k)