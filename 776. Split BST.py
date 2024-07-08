"""
36 ms runtime beats 54.33%
16.50 MB memory beats 64.42%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        if root.val <= target:
            # rnode = root.right
            # root.right = None
            left, right = self.splitBST(root.right, target)
            root.right = left
            return [root, right]
        else:
            left, right = self.splitBST(root.left, target)
            root.left = right
            return [left, root]