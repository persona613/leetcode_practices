"""
42 ms runtime beats 88.19%
16.5 MB memory beats 27.85%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getleafs(self, root):
        res = []
        def dfs(root):
            if not root: return
            if not root.left and not root.right:
                res.append(root.val)
                return
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getleafs(root1) == self.getleafs(root2)