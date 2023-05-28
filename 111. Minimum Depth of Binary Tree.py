"""
494 ms runtime beats 93.8%
49.4 MB memory beats 83.36%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([root])
        d = 1 # depth
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if not curr.left and not curr.right:
                    return d
                if curr.left: 
                    q.append(curr.left)
                if curr.right: 
                    q.append(curr.right)                
            d += 1

