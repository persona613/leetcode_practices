"""
183 ms runtime beats 66.11%
19.28 MB memory beats 84.99%
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        q = deque()
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        E = 2 ** 31 - 1
        while q:
            i, j = q.popleft()
            pre = rooms[i][j]
            for dx, dy in dirs:
                ni = i + dx
                nj = j + dy
                if valid(ni, nj) and rooms[ni][nj] == E:
                    rooms[ni][nj] = pre + 1
                    q.append((ni, nj))        