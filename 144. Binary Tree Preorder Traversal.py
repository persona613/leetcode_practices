"""
27 ms runtime beats 97.8%
13.9 MB memory beats 59.17%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node, output):
        if node == None:
            return output
        output.append(node.val)
        output = self.preorder(node.left, output)
        output = self.preorder(node.right, output) 
        return output
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        return self.preorder(root, output)