"""
207 ms runtime beats 95.62%
37.93 MB memory beats 77.02%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            ln = len(q)
            pre = -inf if level == 0 else inf
            for _ in range(ln):
                curr = q.popleft()
                if level == 0:
                    if curr.val % 2 == 0:
                        return False
                    if curr.val <= pre:
                        return False
                else:
                    if curr.val % 2 == 1:
                        return False
                    if curr.val >= pre:
                        return False
                pre = curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            level ^= 1
        return True