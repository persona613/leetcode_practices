"""
Submission Result: Runtime Error 
Runtime Error Message:
AttributeError: 'NoneType' object has no attribute 'left'
    if not root.left and not root.right:
Line 11 in bst (Solution.py)
    rnode = bst(root.right)
Line 23 in bst (Solution.py)
    return bst(root) != None
Line 32 in isValidBST (Solution.py)
    ret = Solution().isValidBST(param_1)
Line 54 in _driver (Solution.py)
    _driver()
Line 65 in <module> (Solution.py)
Last executed input:
[1,1]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(root):
            if not root.left and not root.right:
                return root
            elif not root.left:
                if root.val < root.right.val:
                    return root
            elif not root.right:
                if root.val > root.left.val:
                    return root
                
            lnode = bst(root.left)
            if not lnode:
                return 
            rnode = bst(root.right)
            if not rnode:
                return 
            if not root.val > lnode.val:
                return 
            if not root.val < rnode.val:
                return 
            return root
        
        return bst(root) != None
        
        

