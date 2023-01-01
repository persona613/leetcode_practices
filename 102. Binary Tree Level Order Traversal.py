"""
47 ms runtime beats 62.9%
14 MB memory beats 99.99%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        que = deque([root])
        while que:
            level = []
            for _ in range(len(que)):
                curr = que.popleft()
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                level.append(curr.val)
            res.append(level)
        return res