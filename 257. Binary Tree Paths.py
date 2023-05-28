"""
43 ms runtime beats 5.42%
13.9 MB memory beats 20.29%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, seen):
            seen += str(node.val)
            if not node.left and not node.right:
                res.append(seen)
                return
            if node.left:
                dfs(node.left, seen+'->')
            if node.right:
                dfs(node.right, seen+'->')
        dfs(root, '')
        return res
