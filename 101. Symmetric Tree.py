"""
39 ms runtime beats 80.92%
14 MB memory beats 60.85%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symcheck(lnode, rnode) -> bool:
            if not lnode and not rnode:
                return True
            elif not lnode or not rnode:
                return False
            elif lnode.val != rnode.val:
                return False
            if not symcheck(lnode.left, rnode.right):
                return False
            if not symcheck(lnode.right, rnode.left):
                return False
            return True
        
        return symcheck(root.left, root.right)
                