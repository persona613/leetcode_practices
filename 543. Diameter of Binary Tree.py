"""
48 ms runtime beats 71.2%
16.2 MB memory beats 98.1%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            nonlocal dia
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            if left + right + 2 > dia:
                dia = left + right + 2
            return max(left, right) + 1
        dia = 0
        dfs(root)
        return dia