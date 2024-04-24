"""
38 ms runtime beats 79.56%
18.20 MB memory beats 79.63%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        last = None
        q = deque([root])
        while q:
            curr = q.popleft()
            last = curr
            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)
        return last.val
            