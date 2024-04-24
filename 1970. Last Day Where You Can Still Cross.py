"""
1917 ms runtime beats 43.22%
27.63 MB memory beats 35.17%
"""
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = len(cells)
        matrix = [[0] * col for _ in range(row)]
        for i in range(n):
            x, y = cells[i]
            matrix[x - 1][y - 1] = i + 1
        
        def run(day):
            stk = []
            seen = set()
            destination = set()
            for j in range(col):
                if matrix[0][j] > day:
                    stk.append((0, j))
                    seen.add((0, j))
            if not stk:
                return False

            for j in range(col):
                if matrix[row - 1][j] > day:
                    destination.add((row - 1, j))
            if not destination:
                return False
            
            while stk:
                ci, cj = stk.pop()
                if (ci, cj) in destination:
                    return True
                for dx, dy in dirs:
                    ni = ci + dx
                    nj = cj + dy
                    if 0 <= ni < row and 0 <= nj < col \
                            and (ni, nj) not in seen \
                            and matrix[ni][nj] > day:
                        seen.add((ni, nj))
                        stk.append((ni, nj))
            return False

        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if run(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r