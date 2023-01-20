""" 
51 ms runtime beats 64.47%
17 MB memory beats 13.64%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(node):            
            if not node:
                return
            
            left = bst(node.left)
            right = bst(node.right)
            
            if left == False or right == False:
                return False
            elif left == None and right == None:
                return [node.val, node.val]
            elif left == None:
                if not node.val < right[0]:
                    return False
                return [node.val, right[1]]
            elif right == None:
                if not node.val > left[1]:
                    return False
                return [left[0], node.val]
            else:
                if not node.val < right[0] or \
                   not node.val > left[1]:
                    return False
                return [left[0], right[1]]
            
        return bst(root) != False
