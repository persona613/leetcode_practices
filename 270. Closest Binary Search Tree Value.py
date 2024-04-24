"""
42 ms runtime beats 62.02%
18.01 MB memory beats 93.39%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        def dfs(node, t):
            nonlocal ans, midf
            if not node: return

            diff = abs(node.val - t)
            if diff < midf:
                midf = diff
                ans = node.val
                if midf == 0: return
            elif diff == midf:
                ans = min(ans, node.val)
            
            if t < node.val:
                dfs(node.left, t)
            else:
                dfs(node.right, t)

        ans = inf
        midf = inf
        dfs(root, target)
        return ans