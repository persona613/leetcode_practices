"""
48 ms runtime beats 72.19%
18.35 MB memory beats 88.16%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        lst = []
        dfs(root)

        ans = inf
        for i in range(1, len(lst)):
            if lst[i] - lst[i-1] < ans:
                ans = lst[i] - lst[i-1]
        return ans