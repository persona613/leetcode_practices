"""
52 ms runtime beats 14.65%
16.2 MB memory beats 62.16%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(root, minn):
            if not root:
                return float('inf')            
            if root.val != minn:
                return root.val
            l = dfs(root.left, minn)
            r = dfs(root.right, minn)
            return min(l, r)
        res = dfs(root, root.val)
        return res if res != float('inf') else -1