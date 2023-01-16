"""
Submission Result: Wrong Answer 
Input:
[5,4,6,null,null,3,7]
Output:
true
Expected:
false
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        elif not root.left:
            return root.val < root.right.val
        elif not root.right:
            return root.val > root.left.val
        
        if not root.val > root.left.val:
            return False
        if not root.val < root.right.val:
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
