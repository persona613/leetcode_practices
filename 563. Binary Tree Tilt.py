"""
71 ms runtime beats 41.79%
18.7 MB memory beats 15.22%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root: return 0
            lsum = dfs(root.left)
            rsum = dfs(root.right)
            ans += abs(lsum-rsum)
            return lsum + rsum + root.val
        dfs(root)
        return ans