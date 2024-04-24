"""
715 ms runtime beats 41.92%
17.18 MB memory beats 66.11%
"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def dfs(node):
            if node in seen:
                return 0
            seen.add(node)
            cnt = 1
            for adj in g[node]:
                cnt += dfs(adj)
            return cnt

        g = defaultdict(list)
        n = len(bombs)
        for i in range(0, n - 1):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, n):
                x2, y2, r2 = bombs[j]
                dist = ((x1-x2) ** 2  + (y1-y2) ** 2) ** 0.5
                if r1 >= dist:
                    g[i].append(j)
                if r2 >= dist:
                    g[j].append(i)
        ans = 0
        for i in range(n):
            seen = set()
            ans = max(ans, dfs(i))
        return ans
