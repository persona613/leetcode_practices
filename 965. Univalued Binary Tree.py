"""
46 ms runtime beats 55.47%
16.5 MB memory beats 7.19%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        # Solution 1
        self.val = root.val
        def dfs(root):
            if not root: 
                return True
            return root.val==self.val and dfs(root.left) and dfs(root.right)
        return dfs(root)

        # Solution 2
        # if not root: return True
        # if root.left and root.val != root.left.val:
        #     return False
        # if root.right and root.val != root.right.val:
        #     return False
        # return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

        # Solution 3
        # if root.left:
        #     if root.left.val != root.val:
        #         return False
        #     if not self.isUnivalTree(root.left):
        #         return False
        # if root.right:
        #     if root.right.val != root.val:
        #         return False
        #     if not self.isUnivalTree(root.right):
        #         return False
        # return True