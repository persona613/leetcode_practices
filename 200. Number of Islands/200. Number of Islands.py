'''
Runtime: 237 ms, faster than 71.88% of Python3 online submissions 
Memory Usage: 19 MB, less than 52.34% of Python3 online submissions
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        # bfs
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    ans += 1
                    q = [(i, j)]
                    while q:
                        ci, cj = q.pop()
                        for dx, dy in dirs:
                            ni = ci + dx
                            nj = cj + dy
                            if 0 <= ni < m and 0 <= nj < n \
                                    and grid[ni][nj] == "1":
                                grid[ni][nj] = "0"
                                q.append((ni, nj))
        return ans                          