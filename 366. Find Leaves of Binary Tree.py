"""
41 ms runtime beats 17.24%
16.48 MB memory beats 64.18%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(node, bag):
            if not node:
                return False
            if not node.left and not node.right:
                bag.append(node.val)
                return True

            if dfs(node.left, bag):
                node.left = None
            if dfs(node.right, bag):
                node.right = None

        dummy = TreeNode(0, root)
        res = []
        while dummy.left:
            bag = []
            dfs(dummy, bag)
            res.append(bag[:])
        return res