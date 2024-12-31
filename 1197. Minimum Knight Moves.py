"""
3455 ms runtime beats 40.50%
78.54 MB memory beats 27.65%
"""
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), 
                (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        seen = {(0, 0)}
        q = deque([(0, 0, 0)])
        while q:
            i, j, step = q.popleft()
            if i == x and j == y:
                return step
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if (ni, nj) not in seen:
                    seen.add((ni, nj))
                    q.append((ni, nj, step + 1))
        return -1
