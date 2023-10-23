"""
39 ms runtime beats 92.20%
16.7 MB memory beats 27.97%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, s):
            if not node: return 0
            if not node.left and not node.right:
                return s*2+node.val
            return dfs(node.left, s*2+node.val) + dfs(node.right, s*2+node.val)
        return dfs(root, 0)