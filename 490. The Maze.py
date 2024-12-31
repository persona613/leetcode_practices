"""
226 ms runtime beats 29.65%
17.34 MB memory beats 49.97%
"""
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        # t: direction, return stop cell
        def roll(ci, cj, t):
            while True:
                ni = ci + dirs[t][0]
                nj = cj + dirs[t][1]
                if not valid(ni, nj) or maze[ni][nj] == 1:
                    break
                ci, cj = ni, nj
            return [ci, cj]

        m = len(maze)
        n = len(maze[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = {tuple(start)}
        q = deque([start])
        while q:
            curr = q.popleft()
            if curr == destination:
                return True
            for t in range(4):
                end = roll(*curr, t)
                if tuple(end) not in seen:
                    seen.add(tuple(end))
                    q.append(end)
        return False