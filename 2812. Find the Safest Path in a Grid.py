"""
5505 ms runtime beats 18.73%
97.50 MB memory beats 5.03%
"""
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        def getnext(i, j):
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if not (0 <= ni < n and 0 <= nj < n):
                    continue
                yield (ni, nj)

        # path to pick cell's score >= mid
        def dfs(i, j, mid, seen):
            if mid == 0:
                return True
            if gf[i][j] < mid:
                return False
            if i == n - 1 and j == n - 1:
                return True
            
            for di, dj in dirs:
                ni = i + di
                nj = j + dj
                if not (0 <= ni < n and 0 <= nj < n):
                    continue
                if (ni, nj) in seen:
                    continue
                seen.add((ni, nj))
                if dfs(ni, nj, mid, seen):
                    return True
            return False

        n = len(grid)
        gf = [[None] * n for _ in range(n)]
        thieves = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    thieves.append((i, j, 0))
                    gf[i][j] = 0

        # cal safe score of each cell
        mxscore = float("-inf")
        dirs = list(zip((1, -1, 0, 0), (0, 0, 1, -1)))
        while thieves:
            ci, cj, sc = thieves.popleft()
            mxscore = max(mxscore, sc)
            for ni, nj in getnext(ci, cj):
                if gf[ni][nj] == None:
                    gf[ni][nj] = sc + 1
                    thieves.append((ni, nj, sc + 1))
        l = 0
        r = mxscore
        while l <= r:
            mid = (l + r) // 2
            if dfs(0, 0, mid, {(0, 0)}):
                l = mid + 1
            else:
                r = mid - 1
        return r