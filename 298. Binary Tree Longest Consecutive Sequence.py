"""
66 ms runtime beats 66.83%
20.24 MB memory beats 13.37%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            nonlocal ans
            ln = 1
            if root.left:            
                l = dfs(root.left)
                if root.val + 1 == root.left.val:
                    l += 1
                    ln = max(ln, l)
            if root.right:
                r = dfs(root.right)
                if root.val + 1 == root.right.val:
                    r += 1
                    ln = max(ln, r)
            if ln > ans:
                ans = ln
            return ln

        ans = 0
        dfs(root)
        return ans