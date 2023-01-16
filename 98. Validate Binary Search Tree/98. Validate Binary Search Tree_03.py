""" 
Submission Result: Wrong Answer 
Input:
[32,26,47,19,null,null,56,null,27]
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
            elif not root.left:
                if not root.val < root.right.val:
                    return
                if side == 0:
                    return max(root.val, root.right.val)
                else:
                    return min(root.val, root.right.val)
            elif not root.right:
                if not root.val > root.left.val:
                    return 
                if side == 0:
                    return max(root.val, root.left.val)
                else:
                    return min(root.val, root.left.val)
            
            lval = bst(root.left, 0)
            if lval == None:
                return 
            rval = bst(root.right, 1)
            if rval == None:
                return
            
            if not root.val > lval or not root.val < rval:
                return            
            if side == 0:
                return max(root.val, lval, rval)
            else:
                return min(root.val, lval, rval)
        
        return bst(root, 0) != None
        
        
