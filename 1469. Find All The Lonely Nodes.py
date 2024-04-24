"""
40 ms runtime beats 89.91%
16.92 MB memory beats 47.48%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node):
            if node.left and node.right:
                dfs(node.left)
                dfs(node.right)
                return
            if node.left:
                res.append(node.left.val)
                dfs(node.left)
            elif node.right:
                res.append(node.right.val)
                dfs(node.right)
            
        res = []
        dfs(root)
        return res