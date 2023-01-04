"""
86 ms runtime beats 34.28%
16.4 MB memory beats 23.2%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        # d denote the depth
        def depth(node, d):
            nonlocal res
            if not node:
                return
            if d > res:
                res = d
            
            depth(node.left, d+1)
            depth(node.right, d+1)
            
        depth(root, 1)
        return res