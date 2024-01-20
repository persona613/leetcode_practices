"""
148 ms runtime beats 69.45%
30.82 MB memory beats 99.74%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, mx):
            if not node:
                return 0
            ans = dfs(node.left, max(mx, node.val)) \
                + dfs(node.right, max(mx, node.val))
            if node.val >= mx:
                ans += 1
            return ans
        return dfs(root, -inf)