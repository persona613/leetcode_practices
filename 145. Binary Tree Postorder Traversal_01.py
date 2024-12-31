"""
29 ms runtime beats 94.43%
13.7 MB memory beats 96.86%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, res):
            if not node:
                return res
            res = dfs(node.left, res)
            res = dfs(node.right, res)
            res.append(node.val) 
            return res
            
        return dfs(root, res)