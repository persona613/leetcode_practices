"""
44 ms runtime beats 70.05%
17.54 MB memory beats 99.98%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def path(node):
            if not node:
                return 0

            l = path(node.left)
            r = path(node.right)
            if l + r > self.dia:
                self.dia = l + r
            return max(l, r) + 1
        
        self.dia = 0
        path(root)
        return self.dia