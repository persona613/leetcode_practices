"""
85 ms runtime beats 82.56%
17.43 MB memory beats 22.32%
"""
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # oi, oj: origin point of subgrid
        # k: grid length
        def helper(grid, oi, oj, k):
            if k == 0:
                return
            
            # detect isLeaf
            val = grid[oi][oj]
            isleaf = True
            sk = 0
            for i in range(oi, oi + k):
                for j in range(oj, oj + k):
                    if grid[i][j] != val:
                        isleaf = False
                        sk = k // 2
                        break
            return Node(
                val, isleaf,
                helper(grid, oi, oj, sk),
                helper(grid, oi, oj + sk, sk),
                helper(grid, oi + sk, oj, sk),
                helper(grid, oi + sk, oj + sk, sk)
                )          

        k = len(grid)
        return helper(grid, 0, 0, k)