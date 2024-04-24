"""
2520 ms runtime beats 5%
154.84 MB memory beats 5.37%
"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        def dfs(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            if i == 0:
                if j == 0 and k == n - 1:
                    memo[(i, j, k)] = grid[0][0] + grid[0][n - 1]
                else:
                    memo[(i, j, k)] = -inf
                return memo[(i, j, k)]

            curr = grid[i][j] + grid[i][k]
            pre = -inf
            for ro1 in range(j - 1, j + 2):
                if ro1 < 0 or ro1 >= n:
                    continue
                for ro2 in range(k - 1, k + 2):
                    if ro2 < 0 or ro2 >= n or ro1 == ro2:
                        continue
                    ret = dfs(i-1, ro1, ro2)
                    if ret > pre:
                        pre = ret
            memo[(i, j, k)] = curr + pre
            return memo[(i, j, k)]

        m = len(grid)
        n = len(grid[0])
        memo = dict()
        ans = 0
        r1_right = 0 + min(m - 1, n - 1)
        r2_left = n - 1 - min(m - 1, n - 1)
        for j in range(0, r1_right + 1):
            for k in range(r2_left, n):
                if j == k: continue
                ret = dfs(m - 1, j, k)
                if ret > ans:
                    ans = ret
        return ans
