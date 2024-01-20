'''
34 ms runtime beats 82.28%
16.18 MB memory beats 83.87%
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stk = [root]
        seen = set()
        res = []
        while stk:
            curr = stk.pop()
            if curr not in seen:
                seen.add(curr)
                if curr.right:
                    stk.append(curr.right)
                stk.append(curr)
                if curr.left:
                    stk.append(curr.left)
            else:
                res.append(curr.val)
        return res
