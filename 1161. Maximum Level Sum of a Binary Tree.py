"""
143 ms runtime beats 95.82%
20.13 MB memory beats 70.70%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        f = defaultdict(list)
        q = deque([root])
        level = 1
        while q:
            ln = len(q)
            tsum = 0
            for _ in range(ln):
                curr = q.popleft()
                tsum += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            f[tsum].append(level)
            level += 1
        k = max(f.keys())
        return f[k][0]
