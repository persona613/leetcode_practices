"""
200 ms runtime beats 43.11%
24.62 MB memory beats 14.99%
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n
            
        q = deque()
        seen = set()
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
                    seen.add((i, j))

        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        while q:
            i, j, d = q.popleft()
            if rooms[i][j] >= d:
                rooms[i][j] = d
                for dx, dy in dirs:
                    ni = i + dx
                    nj = j + dy
                    if valid(ni, nj) and (ni, nj) not in seen:
                        seen.add((ni, nj))
                        q.append((ni, nj, d + 1))        