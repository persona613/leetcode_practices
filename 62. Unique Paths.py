"""
38 ms runtime beats 39.94%
16.83 MB memory beats 6.28%
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i + j == 0:
                return 1
            
            cnt = 0
            if i > 0:
                cnt += dp(i - 1, j)
            if j > 0:
                cnt += dp(i, j - 1)
            return cnt
        
        return dp(m - 1, n - 1)