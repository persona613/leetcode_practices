"""
1863 ms runtime beats 12.69%
17.68 MB memory beats 98.09%
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        # try SPFA(shortest path faster algorithm), bellman ford + queue
        m = len(heights)
        n = len(heights[0])
        effort = [[float("inf")] * n for _ in range(m)]
        effort[0][0] = 0
        inque = [[False] * n for _ in range(m)]
        inque[0][0] = True
        q = deque([(0, 0)])
        dirs = [0, 1, 0, -1, 0]
        while q:
            ci, cj = q.popleft()
            inque[ci][cj] = False
            curr_h = heights[ci][cj]
            curr_cost = effort[ci][cj]
            for d in range(4):
                ni = ci + dirs[d]
                nj = cj + dirs[d + 1]
                if valid(ni, nj):
                    diff = abs(curr_h - heights[ni][nj])
                    if max(curr_cost, diff) < effort[ni][nj]:
                        effort[ni][nj] = max(curr_cost, diff)
                        if inque[ni][nj] is False:
                            q.append((ni, nj))
                            inque[ni][nj] = True
        return effort[-1][-1]