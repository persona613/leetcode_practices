"""
1609 ms runtime beats 19.51%
18.81 MB memory beats 43.45%
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        def valid(x, y):
            if 0 <= x < self.m and 0 <= y < self.n:
                return True
            return False

        def test(d):
            stk = [(0, 0)]
            seen = {(0, 0)}
            while stk:
                curr = stk.pop()
                if curr == (self.m - 1, self.n -1):
                    return True
                for dx, dy in dirs:
                    nx = curr[0] + dx
                    ny = curr[1] + dy
                    if valid(nx, ny) and \
                            (nx, ny) not in seen and \
                            abs(heights[curr[0]][curr[1]] \
                            - heights[nx][ny]) <= d:
                        seen.add((nx, ny))
                        stk.append((nx, ny))
            return False

        mi = 0
        mx = max(max(row) for row in heights)
        self.m = len(heights)
        self.n = len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while mi <= mx:
            mid = (mi + mx) // 2
            if test(mid):
                mx = mid - 1
            else:
                mi = mid + 1
        return mi