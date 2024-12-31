"""
77 ms runtime beats 80.08%
17.62 MB memory beats 96.09%
"""
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [(rStart, cStart)]
        cnt = rows * cols
        # [Right, Down, Left, Up]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        idx = 0
        # two directions add one step: 1,1,2,2,3,3,4,4,5...
        step = 1
        ci, cj = rStart, cStart
        while len(res) < cnt:
            di, dj = dirs[idx]
            for _ in range(step):
                ci = ci + di
                cj = cj + dj
                if 0 <= ci < rows and 0 <= cj < cols:
                    res.append((ci, cj))

            if idx % 2 == 1:
                step += 1
            idx = (idx + 1) % 4
        return res