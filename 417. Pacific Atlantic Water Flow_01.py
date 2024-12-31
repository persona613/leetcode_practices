"""
Wrong Answer
59 / 113 testcases passed

Editorial
Input
heights =
[[2,1],[1,2]]

Use Testcase
Output
[[0,0],[1,1]]
Expected
[[0,0],[0,1],[1,0],[1,1]]
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        if m == 1 or n == 1:
            res = []
            for i in range(m):
                for j in range(n):
                    res.append([i, j])
            return res
            
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        # color maps, Pacific = 1, Atlantic = 2
        maps = [[0] * n for _ in range(m)]

        # BFS source: (i, j, color code)
        q = deque()
        for j in range(n):
            maps[0][j] = 1
            q.append((0, j, 1))
            maps[m - 1][j] = 2
            q.append((m - 1, j, 2))
        for i in range(m):
            maps[i][0] = 1
            q.append((i, 0, 1))
            maps[i][n - 1] = 2
            q.append((i, n - 1, 2))

        while q:
            ci, cj, color = q.popleft()
            for di, dj in dirs:
                ni = ci + di
                nj = cj + dj
                if (ni < 0 or ni >= m or nj < 0 or nj >= n
                    or heights[ni][nj] < heights[ci][cj]
                    or maps[ni][nj] == color
                    or maps[ni][nj] == 3):
                    continue
                maps[ni][nj] += color
                q.append((ni, nj, color))
        
        res = []
        for i in range(m):
            for j in range(n):
                if maps[i][j] == 3:
                    res.append([i, j])
        return res