"""
Wrong Answer
30 / 43 testcases passed
Input
grid =
[[3,2],[0,1]]

Use Testcase
Output
1
Expected
3
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def swim(i, j, time):
            nonlocal n
            if i == n - 1 and j == n - 1:
                return True
            for dx, dy in dirs:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < n \
                        and grid[nx][ny] not in seen \
                        and grid[nx][ny] <= time:
                    seen.add(grid[nx][ny])
                    if swim(nx, ny, time):
                        return True
            return False
        
        n = len(grid)
        l = 0
        r = n ** 2
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while l <= r:
            mid = (l + r) // 2
            seen = {grid[0][0]}
            if swim(0, 0, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l