"""
40 ms runtime beats 20.33%
16.58 MB memory beats 20.02%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        res = []
        stk = [root]
        seen = set()
        while stk:
            curr = stk.pop()
            if curr not in seen:
                seen.add(curr)
                stk.append(curr)
                if curr.right:
                    stk.append(curr.right)
                if curr.left:
                    stk.append(curr.left)
            else:
                res.append(curr.val)
        return res