"""
54 ms runtime beats 15.13%
17.81 MB memory beats 37.96%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stk = [(root, False)]
        depth = dict()
        while stk:
            node, seen = stk.pop()
            if not node:
                continue
            if not seen:
                stk.append((node, True))
                stk.append((node.right, False))
                stk.append((node.left, False))
            else:
                l = depth.get(node.left, 0)
                r = depth.get(node.right, 0)
                ans = max(ans, l + r)
                depth[node] = max(l, r) + 1
        return ans