"""
334 ms runtime beats 73.00%
38.31 MB memory beats 71.35%
"""
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        def spy(i, j):
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                while  0 <= ni < m and 0 <= nj < n:
                    if mat[ni][nj] in [1, 2]:
                        break
                    mat[ni][nj] = 3
                    ni += di
                    nj += dj

        mat = [[0] * n for _ in range(m)]
        for wall in walls:
            mat[wall[0]][wall[1]] = 1
        for guard in guards:
            mat[guard[0]][guard[1]] = 2
        
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        for i, j in guards:
            spy(i, j)

        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans += 1
        return ans