"""
57 ms runtime beats 82.04%
16.57 MB memory beats 74.82%
"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            for j in range(3):
                if j == 0:
                    costs[i][j] += min(costs[i-1][1], costs[i-1][2])
                elif j == 1:
                    costs[i][j] += min(costs[i-1][0], costs[i-1][2])
                else:
                    costs[i][j] += min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1])