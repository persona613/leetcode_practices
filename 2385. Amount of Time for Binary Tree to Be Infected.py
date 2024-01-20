"""
437 ms runtime beats 81.01%
68.27 MB memory beats 59.78%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        gf = defaultdict(set)
        dq = deque([root])
        while dq:
            curr = dq.popleft()
            if curr.left:
                dq.append(curr.left)
                gf[curr.val].add(curr.left.val)
                gf[curr.left.val].add(curr.val)
            if curr.right:
                dq.append(curr.right)
                gf[curr.val].add(curr.right.val)
                gf[curr.right.val].add(curr.val)
        dq = deque([start])
        seen = set()
        t = 0
        while dq:
            t += 1
            for _ in range(len(dq)):
                curr = dq.popleft()
                seen.add(curr)
                for v in gf[curr]:
                    if v not in seen:
                        dq.append(v)
        return t - 1