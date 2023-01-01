"""
47 ms runtime beats 83.4%
15.2 MB memory beats 16.52%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def valsum(node: TreeNode, sval: int) -> bool:
            if not node:
                return False
            sval += node.val
            if not node.left and not node.right:
                if sval == targetSum:
                    return True
                else:
                    return False
            
            if valsum(node.left, sval) or valsum(node.right, sval):
                return True
            else:
                return False
        return valsum(root, 0)