"""
32 ms runtime beats 90.18%
16.54 MB memory beats 38.65%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        # if val=0, return one image coin (-1) with cost 1
        # if val=1, return 0
        # if val>1, return real coin (val-1) with cost val-1
        # if image coinmeet real coin => cancel both, return remain coins
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            remain = l + r
            if node.val == 0:
                remain -= 1
            elif node.val > 1:
                remain += node.val - 1
            ans[0] += abs(remain)
            return remain

        ans = [0]
        dfs(root)
        return ans[0]