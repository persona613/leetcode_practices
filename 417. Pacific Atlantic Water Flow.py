"""
205 ms runtime beats 78.06%
18.18 MB memory beats 65.27%
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        # color maps, Pacific = 1, Atlantic = 2
        maps = [[0] * n for _ in range(m)]

        # BFS source: (i, j, color code)
        q = deque()
        for j in range(n):
            q.append((0, j, 1))
            q.append((m - 1, j, 2))
        for i in range(m):
            q.append((i, 0, 1))
            q.append((i, n - 1, 2))

        while q:
            ci, cj, color = q.popleft()
            # seen
            if maps[ci][cj] == color or maps[ci][cj] == 3:
                continue
            maps[ci][cj] += color
            
            for di, dj in dirs:
                ni = ci + di
                nj = cj + dj
                if (ni < 0 or ni >= m or nj < 0 or nj >= n
                    or heights[ni][nj] < heights[ci][cj]):
                    continue
                q.append((ni, nj, color))
        
        res = []
        for i in range(m):
            for j in range(n):
                if maps[i][j] == 3:
                    res.append([i, j])
        return res