"""
31 ms runtime beats 82.21%
16.56 MB memory beats 26.23%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, val):
            nonlocal ans
            if not node:
                return
            val = val * 10 + node.val
            if not node.left and not node.right:
                ans += val
                return
            
            dfs(node.left, val)
            dfs(node.right, val)
        
        ans = 0
        dfs(root, 0)
        return ans