"""
46 ms runtime beats 48.21%
18.21 MB memory beats 22.84%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        # ret = [cnt, min_val, max_val]
        def dfs(root):
            nonlocal maxi
            if not root: return [0, inf, -inf]

            lt = dfs(root.left)
            rt = dfs(root.right)

            # curr tree is bst
            if lt[2] < root.val and rt[1] > root.val:
                cnt = 1 + lt[0] + rt[0]
                mi = min(root.val, lt[1])
                mx = max(root.val, rt[2])
                if cnt > maxi:
                    maxi = cnt
                return [cnt, mi, mx]
            return [-1, -inf, inf]

        if not root: return 0
        maxi = 1
        dfs(root)
        return maxi