"""
49 ms runtime beats 41.92%
18.08 MB memory beats 69.25%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # [rob curr, not rob curr]
        def dfs(node):
            if not node: return [0, 0]
            
            l = dfs(node.left)
            r = dfs(node.right)
            # take curr, not take curr
            tk = node.val + l[1] + r[1]
            ntk = max(l) + max(r)
            return [tk, ntk]

        return max(dfs(root))