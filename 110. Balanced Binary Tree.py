"""
49 ms runtime beats 89.10%
18.6 MB memory beats 58.89%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def h(root):
            if not root:
                return -1
            left = h(root.left)
            right = h(root.right)

            if left == None or right == None:
                return 
            if abs(left-right) > 1:
                return 
            return max(left, right) + 1        

        return h(root) != None
            