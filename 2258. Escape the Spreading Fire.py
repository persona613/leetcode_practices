"""
645 ms runtime beats 31.17%
18.63 MB memory beats 55.47%
"""
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:

        def valid(i, j):
            nonlocal m, n
            return 0 <= i < m and 0 <= j < n

        def run(start):
            nonlocal m, n
            # q = (i, j, start_time)
            q = deque([(0, 0, start)])
            seen = {(0, 0)}
            while q:
                ci, cj, time = q.popleft()
                for di, dj in dirs:
                    ni = ci + di
                    nj = cj + dj
                    if valid(ni, nj):
                        # safe in time
                        if (ni, nj) == (m - 1, n - 1) \
                                and firetime[m - 1][n - 1] >= time + 1:
                            return True
                        elif (ni, nj) not in seen \
                                and firetime[ni][nj] > time + 1:
                            seen.add((ni, nj))
                            q.append((ni, nj, time + 1))
            return False

        m = len(grid)
        n = len(grid[0])
        # firetime: inf=no fire, -2=wall
        firetime = [[inf] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    firetime[i][j] = 0
                elif grid[i][j] == 2:
                    firetime[i][j] = -2

        dirs = list(zip((0, 0, 1, -1), (1, -1, 0, 0)))
        t = 1
        while q:
            ln = len(q)
            for _ in range(ln):
                ci, cj = q.popleft()
                for di, dj in dirs:
                    ni = ci + di
                    nj = cj + dj
                    if valid(ni, nj) and firetime[ni][nj] == inf:
                        firetime[ni][nj] = t
                        q.append((ni, nj))
            t += 1

        l = 0
        r = m * n
        while l <= r:
            mid = (l + r) // 2
            # print(f"l={l},r={r},mid={mid},ret={run(mid)}")
            if run(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r if r < m * n else 10 ** 9