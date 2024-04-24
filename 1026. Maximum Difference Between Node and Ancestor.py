"""
45 ms runtime beats 31.83%
17.97 MB memory beats 99.80%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def helper(node, cmi, cmx):
            if not node:
                return cmx - cmi
            cmi = min(cmi, node.val)
            cmx = max(cmx, node.val)
            l = helper(node.left, cmi, cmx)
            r = helper(node.right, cmi, cmx)
            return max(l, r)

        return helper(root, root.val, root.val)