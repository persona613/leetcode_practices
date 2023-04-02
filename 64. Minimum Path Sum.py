"""
120 ms runtime beats 31.1%
16.1 MB memory beats 21.52%
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        def pos(i, j):
            if memo[i][j]:
                return memo[i][j]
            if i == 0 and j == 0:
                memo[i][j] = grid[i][j]
                return memo[i][j]

            if i-1 < 0:
                memo[i][j] = pos(i, j-1) + grid[i][j]
            elif j-1 < 0:
                memo[i][j] = pos(i-1, j) + grid[i][j]
            else:
                memo[i][j] = min(pos(i-1, j), pos(i, j-1)) + grid[i][j]
            return memo[i][j]
        
        memo = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ans = pos(len(grid)-1, len(grid[0])-1)
        return ans
