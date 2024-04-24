"""
693 ms runtime beats 55.43%
18.15 MB memory beats 43.88%
"""
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n \
                   and maze[i][j] == "."
        def isexit(i, j):
            return (i == 0 or i == m - 1 or j == 0 or j == n - 1 ) \
                   and maze[i][j] == "."

        m = len(maze)
        n = len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # path written in node
        q = deque([(entrance[0], entrance[1], 0)])
        seen = {(entrance[0], entrance[1])}
        while q:
            i, j, p = q.popleft()
            if isexit(i, j) and p > 0:
                return p
            
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if valid(ni, nj) and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    q.append((ni, nj, p + 1))
        return -1