"""
46 ms runtime beats 34.7%
15.3 MB memory beats 38.71%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)
        
        if not root.left:
            return
        curr = root.left
        while curr.right:
            curr = curr.right
        curr.right = root.right
        root.right = root.left
        root.left = None