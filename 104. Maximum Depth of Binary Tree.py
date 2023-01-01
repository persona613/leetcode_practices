"""
41 ms runtime beats 93.47%
16.2 MB memory beats 76.45%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(node) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            l = depth(node.left)
            r = depth(node.right)
            return max(l,r)+1
        
        return depth(root)