"""
52 ms runtime beats 32.90%
16.4 MB memory beats 36.72%
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ds = [(0,1),(1,0),(0,-1),(-1,0)]
        res = [[None for _ in range(n)] for _ in range(n)]
        i, j, k = 0, 0, 0
        di, dj = ds[k]
        for v in range(1, n**2+1):
            res[i][j] = v
            # test next index
            ti, tj = i+di, j+dj
            if ti<0 or ti>=n or tj<0 or tj>=n or res[ti][tj]!=None:
                k += 1
                di, dj = ds[k%4]
            i += di
            j += dj
        return res