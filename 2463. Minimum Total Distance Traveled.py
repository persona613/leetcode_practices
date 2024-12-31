"""
2684 ms runtime beats 8.00%
447.96 MB memory beats 5.44%
"""
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robots = sorted(robot)
        sorted_factories = sorted(factory)
        factories = [f[0] for f in sorted_factories]
        counts = [f[1] for f in sorted_factories]
        m = len(robots)
        n = len(factories)

        @lru_cache(None)
        def dp(i, j, h):
            if i == m:
                return 0
            if j == n:
                return float("inf")
            
            dist = float("inf")
            # used curr factory
            if h > 0:
                dt1 = abs(robots[i] - factories[j]) + dp(i + 1, j, h - 1)
                dist = min(dist, dt1)
            # not used curr factory
            if j < n - 1:
                dt2 = dp(i, j + 1, counts[j + 1])
                dist = min(dist, dt2)
            return dist

        return dp(0, 0, counts[0])