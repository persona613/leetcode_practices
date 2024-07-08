"""
53 ms runtime beats 17.86%
17.74 MB memory beats 16.85%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return True, 0
            
            lbool, lh = height(root.left)
            rbool, rh = height(root.right)
            if lbool and rbool:
                return abs(lh - rh) <= 1, max(lh, rh) + 1
            return False, max(lh, rh) + 1

        return height(root)[0]            
            