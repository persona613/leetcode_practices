"""
39 ms runtime beats 81.48%
19.09 MB memory beats 74.81%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            nonlocal ans
            mi = mx = node.val
            if not node.left and not node.right:
                return mi, mx

            if node.left:
                lmi, lmx = dfs(node.left)
                d = max(abs(node.val-lmi), abs(node.val-lmx))
                ans = max(ans, d)
                mi = min(mi, lmi)
                mx = max(mx, lmx)
            if node.right:
                rmi, rmx = dfs(node.right)
                d = max(abs(node.val-rmi), abs(node.val-rmx))
                ans = max(ans, d)
                mi = min(mi, rmi)
                mx = max(mx, rmx)
            return mi, mx
            
        ans = 0
        dfs(root)
        return ans