"""
30 ms runtime beats 90.67%
16.75 MB memory beats 47.79%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node, isleft: bool) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if isleft else 0

            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)