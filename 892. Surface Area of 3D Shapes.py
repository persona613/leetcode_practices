"""
206 ms runtime beats 5.80%
16.9 MB memory beats 9.37%
"""
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        top, front, left = n**2, 0, 0
        for i in range(n):
            rmax = max(grid[i])
            for j in range(n):
                if grid[i][j] == 0:
                    top -= 1
            left += rmax
        for col in zip(*grid):
            front += max(col)
        self.rowcave, self.colcave = set(), set()
        cave = 0
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if (i, j) not in self.rowcave:
                    lout, lv = self.detect(i, j, v, 0, -1, grid)
                    if lout:
                        rout, rv = self.detect(i, j, v, 0, 1, grid)
                        if rout:
                            cave += (min(lv,rv)-v)*2
                            # print(i,j,"row",(min(lv,rv)-v)*2)
                    self.rowcave.add((i, j))
                if (i, j) not in self.colcave:
                    tout, tv = self.detect(i, j, v, -1, 0, grid)
                    if tout:
                        dout, dv = self.detect(i, j, v, 1, 0, grid)
                        if dout:
                            cave += (min(tv, dv)-v)*2
                            # print(i,j,"col",(min(tv,dv)-v)*2)
                    self.colcave.add((i, j))
        # print(top, front, left, cave)
        return (top+front+left)*2+cave
    # detect boundry, return bool, height
    def detect(self, i, j, v, di, dj, grid):
        i += di
        j += dj
        if di == 0:
            pool = self.rowcave
        else:
            pool = self.colcave
        while -1<i<len(grid) and -1<j<len(grid):
            if v < grid[i][j]:
                return True, grid[i][j]
            elif v == grid[i][j]:
                pool.add((i, j))
            i += di
            j += dj
        return False, 0