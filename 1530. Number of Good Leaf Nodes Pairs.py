"""
104 ms runtime beats 53.23%
16.95 MB memory beats 38.59%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def dfs(node, distance):
            nonlocal ans
            # array index = left node's depth from bottom
            # array value = left node's count
            if not node:
                return [0] * 10
            # base case: 1 left-node at dist 1
            if not node.left and not node.right:
                return [1] + [0] * 9

            la = dfs(node.left, distance)
            ra = dfs(node.right, distance)

            # shortest dist between left nodes is 2
            for total_dist in range(2, distance + 1):
                for k in range(1, total_dist):
                    # -1 for array zero index
                    ans += la[k - 1] * ra[total_dist - k - 1]

            # merge two array, 0 left-node at depth 1
            # every depth + 1, drop depth > 10
            new = [0]
            for i in range(len(la) - 1):
                new.append(la[i] + ra[i])
            return new

        ans = 0
        dfs(root, distance)
        return ans