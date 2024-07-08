"""
59 ms runtime beats 59.19%
18.45 MB memory beats 76.41%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        curr = root
        sm = 0
        while stack or curr is not None:

            if not curr:
                curr = stack.pop()
            else:
                while curr.right:
                    stack.append(curr)
                    curr = curr.right
                    
            sm += curr.val
            curr.val = sm
            curr = curr.left
        
        return root