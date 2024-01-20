"""
62 ms runtime beats 12.30%
17.48 MB memory beats 83.96%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0, 0
            lsum, lcnt = dfs(node.left)
            rsum, rcnt = dfs(node.right)
            tsum = lsum + rsum + node.val
            tcnt = lcnt + rcnt + 1
            if node.val == tsum//tcnt:
                ans += 1
            return tsum, tcnt
            
        dfs(root)
        return ans