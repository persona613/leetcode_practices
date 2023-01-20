"""
144 ms runtime beats 62.61%
16.9 MB memory beats 90.63%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def search(node, val):
            if not node:
                return TreeNode(val)
            if val > node.val:
                if search(node.right, val):
                    node.right = search(node.right, val)
            else:
                if search(node.left, val):
                    node.left = search(node.left, val)   
                    
        if not root:
            return TreeNode(val)
        search(root, val)        
        return  root
        