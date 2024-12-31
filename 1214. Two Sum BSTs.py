"""
54 ms runtime beats 77.70%
19.82 MB memory beats 19.43%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def collect(root):
            if root:
                bag.add(target - root.val)
                collect(root.left)
                collect(root.right)

        def search(root):
            if not root:
                return
            if root.val in bag:
                return True
            return search(root.left) or search(root.right)

        bag = set()
        collect(root1)
        return search(root2)