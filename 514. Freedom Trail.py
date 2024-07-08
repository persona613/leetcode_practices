"""
105 ms runtime beats 70.19%
17.42 MB memory beats 33.33%
"""
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # p = pre char's position, i = curr index of key
        @cache
        def dfs(i, p):
            if i == n:
                return 0

            candidates = dic[key[i]]
            mi_dist = inf
            for candi in candidates:
                dist = abs(candi - p)
                # clockwise and anti-clockwise
                dist = min(dist, m - dist)
                dist += dfs(i + 1, candi)

                mi_dist = min(mi_dist, dist)
            return mi_dist + 1

        dic = defaultdict(list)
        for i, c in enumerate(ring):
            dic[c].append(i)
        m = len(ring)
        n = len(key)
        return dfs(0, 0)