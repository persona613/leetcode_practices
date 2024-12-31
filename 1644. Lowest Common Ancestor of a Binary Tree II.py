"""
145 ms runtime beats 59.53%
22.28 MB memory beats 6.09%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return

            l = dfs(node.left)
            r = dfs(node.right)
            if l and r:
                res[0] = node
            elif (node == p or node == q) and (l or r):
                res[0] = node
            return l or r or node == p or node == q

        res = [None]
        dfs(root)
        return res[0]