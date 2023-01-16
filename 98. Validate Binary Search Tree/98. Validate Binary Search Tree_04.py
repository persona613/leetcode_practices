""" 
Submission Result: Wrong Answer 
Input:
[120,70,140,50,100,130,160,20,55,75,110,119,135,150,200]
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
        # 0 is left subtree, 1 is right subtree
        def bst(root, side):
            if not root.left and not root.right:
                return root.val
            
            lval = "#"
            rval = "#"
            if root.left:
                lval = bst(root.left, 0)
                if lval == None or not root.val > lval:
                    return 
            if root.right:
                rval = bst(root.right, 1)
                if rval == None or not root.val < rval:
                    return
           
            if side == 0:
                if lval == "#":
                    return max(root.val, rval)
                elif rval == "#":
                    return max(root.val, lval)
                return max(root.val, lval, rval)
            else:
                if lval == "#":
                    return min(root.val, rval)
                elif rval == "#":
                    return min(root.val, lval)
                return min(root.val, lval, rval)
        
        return bst(root, 0) != None
        
        

