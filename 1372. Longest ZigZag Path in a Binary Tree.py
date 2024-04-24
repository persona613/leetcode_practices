"""
172 ms runtime beats 92.24%
30.45 MB memory beats 82.41%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        # path: left=0, right=1
        def dfs(node, path, cnt):
            nonlocal ans
            if not node:
                if cnt - 1 > ans:
                    ans = cnt - 1
                return
            
            # path form left
            if path == 0:
                dfs(node.right, 1 - path, cnt + 1)
                dfs(node.left, path, 1)

            # path from right
            else:
                dfs(node.left, 1 - path, cnt + 1)
                dfs(node.right, path, 1)
        ans = 0
        dfs(root, 0, 0)
        return ans