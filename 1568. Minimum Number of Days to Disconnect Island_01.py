"""
Wrong Answer
97 / 99 testcases passed

Editorial
Input
grid =
[[1,1],[1,0]]

Use Testcase
Output
2
Expected
1
"""
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        dirs = list(zip((0, 1, 0, -1), (1, 0, -1, 0)))
        def dfs(i, j, seen):
            for di, dj in dirs:
                ci = i + di
                cj = j + dj
                if valid(ci, cj) and grid[ci][cj] == 1 \
                        and (ci, cj) not in seen:
                    seen.add((ci, cj))
                    dfs(ci, cj, seen)

        # detect how many components
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    dfs(i, j, seen)
                    cnt += 1
        if cnt != 1:
            return 0
        if len(seen) < 3:
            return len(seen)

        def possibile(i, j):
            # left and right
            if j - 1 >= 0 and grid[i][j - 1] == 1 \
                    and j + 1 < n and grid[i][j + 1] == 1:
                return True
            # up and down
            if i - 1 >= 0 and grid[i - 1][j] == 1 \
                    and i + 1 < m and grid[i + 1][j] == 1:
                return True
            return False

        def scan():
            x, y = seen.pop()
            bag = {(x, y)}
            dfs(x, y, bag)
            
            seen.add((x, y))
            return len(bag) < len(seen)

        # test delete each cell
        for i, j in seen:
            # filter possible cell
            if possibile(i, j):
                seen.remove((i, j))
                grid[i][j] = 0
                
                # check disconnect by scan land's count
                if scan():
                    return 1
                seen.add((i, j))
                grid[i][j] = 1
        return 2
