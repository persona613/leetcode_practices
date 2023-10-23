"""
132 ms runtime beats 96.42%
16.68 MB memory beats 76.22%
"""
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m*n
        if k == 0:
            return grid

        arr = []
        for r in grid:
            arr += r
        arr = arr[-k:] + arr[:-k]
        
        res = []
        i = 0
        for _ in range(m):
            res.append(arr[i:i+n])
            i += n
        return res
