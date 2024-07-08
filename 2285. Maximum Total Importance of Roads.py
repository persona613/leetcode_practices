"""
1177 ms runtime beats 95.90%
42.18 MB memory beats 57.79%
"""
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1

        # assign value according degree
        degree.sort()
        ans = 0
        for i in range(n):
            ans += degree[i] * (i + 1)
        return ans