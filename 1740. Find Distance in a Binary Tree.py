"""
38 ms runtime beats 100%
21.09 MB memory beats 40.95%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        # for recursive return
        # dist is negtive befor LCA, postive after LCA
        if not root:
            return 0

        l = self.findDistance(root.left, p, q)
        r = self.findDistance(root.right, p, q)

        # curr is LCA, pq at different branch, turn dist positive
        if l and r:
            return abs(l + r)
        if p != q and (root.val == p or root.val == q):
            # curr is LCA, pq at same branch, turn dist positive
            if l or r:
                return abs(l + r)
            # find only p or q
            return -1
        # before LCA, add dist -1
        if l < 0 or r < 0:
            return l + r - 1
        # after LCA or not find any dist of p or q
        return l + r
        