"""
657 ms runtime beats 78.62%
17.08 MB memory beats 90.63%
"""
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n \
                   and maze[i][j] == "."
        def isexit(i, j):
            return i == 0 or i == m - 1 or j == 0 or j == n - 1

        m = len(maze)
        n = len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        maze[entrance[0]][entrance[1]] = "+"
        q = deque([(entrance[0], entrance[1], 0)])
        while q:
            i, j, p = q.popleft()
            
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if valid(ni, nj):
                    if isexit(ni, nj):
                        return p + 1
                    
                    maze[ni][nj] = "+"
                    q.append((ni, nj, p + 1))
        return -1