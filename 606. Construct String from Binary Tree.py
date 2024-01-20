"""
52 ms runtime beats 60.87%
19.21 MB memory beats 6.21%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
          if not node: return
          res.append(str(node.val))
          if not node.left and not node.right:
            return
          res.append("(")
          dfs(node.left)
          res.append(")")
          if node.right:
            res.append("(")
            dfs(node.right)
            res.append(")")
        
        res = []
        dfs(root)
        return "".join(res)