"""
52 ms runtime beats 86.62%
18.9 MB memory beats 25.76%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([root])
        while q:
            sums = 0
            cnt = len(q)
            for _ in range(cnt):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                sums += curr.val
            res.append(sums/cnt)
        return res