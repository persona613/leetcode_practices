"""
49 ms runtime beats 70.28%
16.3 MB memory beats 23.2%
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
        # d denote the depth-1
        def depth(node, d):
            nonlocal res
            if not node:
                res = max(res,d)
                return
            
            depth(node.left, d+1)
            depth(node.right, d+1)
            
        depth(root, 0)
        return res