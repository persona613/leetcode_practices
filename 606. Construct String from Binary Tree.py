"""
79 ms runtime beats 5.39%
18.8 MB memory beats 33.25%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root.left and not root.right:
            return str(root.val)
        ss = [str(root.val)]
        if root.left:
            ls = self.tree2str(root.left)
            ss.extend(['(', ls, ')'])
        else:
            ss.append('()')
        if root.right:
            rs = self.tree2str(root.right)
            ss.extend(['(', rs, ')'])
        return ''.join(ss)