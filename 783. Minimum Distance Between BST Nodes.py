"""
49 ms runtime beats 54.58%
16.5 MB memory beats 30.15%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans = 100000
        def dfs(root):
            nonlocal ans
            if not root.left and not root.right:
                return [root.val, root.val]
            tmp = [root.val]
            if root.left:
                lrange = dfs(root.left)
                ans = min(ans, root.val-lrange[1])
                tmp.extend(lrange)
            if root.right:
                rrange = dfs(root.right)
                ans = min(ans, rrange[0]-root.val)
                tmp.extend(rrange)
            return [min(tmp), max(tmp)]        
        dfs(root)
        return ans