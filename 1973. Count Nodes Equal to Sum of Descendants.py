"""
309 ms runtime beats 88.33%
50.30 MB memory beats 74.17%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0

            ts = dfs(node.left) + dfs(node.right)
            if node.val == ts:
                self.cnt += 1
            return ts + node.val

        self.cnt = 0
        dfs(root)
        return self.cnt