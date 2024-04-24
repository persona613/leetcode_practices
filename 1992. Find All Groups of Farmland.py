"""
866 ms runtime beats 54.60%
35.88 MB memory beats 25.03%
"""
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        def dfs(i, j):
            nonlocal r2, c2
            if i + 1 < m and land[i + 1][j] == 1 \
                    and (i + 1, j) not in seen:
                seen.add((i + 1, j))
                r2 = max(r2, i + 1)
                dfs(i + 1, j)
            if j + 1 < n and land[i][j + 1] == 1 \
                    and (i, j + 1) not in seen:
                seen.add((i, j + 1))
                c2 = max(c2, j + 1)
                dfs(i, j + 1)

        m = len(land)
        n = len(land[0])
        seen = set()
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    r2 = i
                    c2 = j
                    dfs(i, j)
                    res.append([i, j, r2, c2])
        return  res