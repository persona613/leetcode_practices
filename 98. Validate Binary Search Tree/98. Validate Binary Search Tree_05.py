""" 
50 ms runtime beats 74.36%
16.5 MB memory beats 43.74%
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
            
            if not node.left and not node.right:
                return [node.val, node.val]
            
            lside = rside = None # [min_val, max_val]
            if node.left:
                if not node.val > node.left.val:
                    return False
                lside = bst(node.left)
                if lside == False:
                    return False
            if node.right:
                if not node.val < node.right.val:
                    return False
                rside = bst(node.right)
                if rside == False:
                    return False
                
            ret = [node.val]    
            if lside == None:
                if not node.val < rside[0]:
                    return False
                else:
                    ret.extend(rside)
                    return [min(ret), max(ret)]
            elif rside == None:
                if not node.val > lside[1]:
                    return False
                else:
                    ret.extend(lside)
                    return [min(ret), max(ret)]
            elif lside and rside:
                if not node.val < rside[0] or \
                   not node.val > lside[1]:
                    return False
                else:
                    ret.extend(lside)
                    ret.extend(rside)
                    return [min(ret), max(ret)]
                
        return bst(root) != False
                    
                
            

        

            
        
            
            
 
        
        

