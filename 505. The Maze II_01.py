"""
Wrong Answer
73 / 79 testcases passed
"""
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        m = len(maze)
        n = len(maze[0])
        seen = [[0] * n for _ in range(m)]
        seen[start[0]][start[1]] = True
        dirX = [1, -1, 0, 0]
        dirY = [0, 0, 1, -1]

        # dijkstra min heap: [step, i, j]
        q = [[0, start[0], start[1]]]
        while q:
            step, ci, cj = heappop(q)
            if ci == destination[0] and cj == destination[1]:
                return step
            for t in range(4):
                row = ci
                col = cj
                move = step
                while valid(row, col) and maze[row][col] == 0:
                    row += dirX[t]
                    col += dirY[t]
                    move += 1
                row -= dirX[t]
                col -= dirY[t]
                move -= 1
                if not seen[row][col]:
                    seen[row][col] = True
                    heappush(q, [move, row, col])
        return -1




        