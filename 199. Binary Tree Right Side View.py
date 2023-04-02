"""
41 ms runtime beats 30.94%
13.9 MB memory beats 62.25%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def rightside(node):
            if not node:
                return
            q = deque([node])
            while q:
                # right most index
                rmost = len(q)-1
                for i in range(len(q)):
                    curr = q.popleft()
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                    if i == rmost:
                        res.append(curr.val)        
        res = []
        rightside(root)
        return res