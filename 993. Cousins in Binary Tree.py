"""
38 ms runtime beats 91.92%
16.3 MB memory beats 92.1%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root, 0)]) # (root, parent.val)
        ps = [] # parent.val
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr[0].val == x or curr[0].val == y:
                    ps.append(curr[1]) 
                if curr[0].left:
                    q.append((curr[0].left, curr[0].val)) 
                if curr[0].right:
                    q.append((curr[0].right, curr[0].val))
            if not len(ps):
                pass
            elif len(ps) == 1:
                return False
            else: #len(ps) == 2
                return ps[0] != ps[1]