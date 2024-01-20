"""
54 ms runtime beats 52.98%
19.12 MB memory beats 63.01%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        ans = -inf
        def dfs(node):
            nonlocal ans
            if not node:
                return 0, 0
            # sum, cnt
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            sm = ls + rs + node.val
            tc = lc + rc + 1
            if sm / tc > ans:
                ans = sm / tc
            return sm, tc
        dfs(root)
        return ans