"""
49 ms runtime beats 5.35%
17.3 MB memory beats 5.53%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        # left child = 1, right child = 0
        def dfs(root: Optional[TreeNode], child: int) -> int:
            nonlocal ans
            if not root.left and not root.right and child == 1:
                ans += root.val
            if root.left:
                dfs(root.left, 1)
            if root.right:
                dfs(root.right, 0)
        dfs(root, 0)
        return ans

