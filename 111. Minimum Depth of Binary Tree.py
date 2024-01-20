"""
223 ms runtime beats 96.33%
43.58 MB memory beats 99.68%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        if root.left:
            return self.minDepth(root.left) + 1
        return self.minDepth(root.right) + 1


