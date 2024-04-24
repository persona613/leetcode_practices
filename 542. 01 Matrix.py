"""
483 ms runtime beats 62.12%
19.13 MB memory beats 90.35%
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def valid(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False

        m = len(mat)
        n = len(mat[0])
        q = deque()
        seen = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 1))
                    
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            ln = len(q)
            for _ in range(ln):
                i, j, p = q.popleft()
                for dx, dy in dirs:
                    ni = i + dx
                    nj = j + dy
                    if valid(ni, nj) and mat[ni][nj] == 1 \
                        and (ni, nj) not in seen:

                        seen.add((ni, nj))
                        mat[ni][nj] = p
                        q.append((ni, nj, p + 1))
        return mat
