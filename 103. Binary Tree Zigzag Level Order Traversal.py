"""
33 ms runtime beats 87.46%
16.81 MB memory beats 56.32%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        lv = 0
        while q:
            tmp = []
            for _ in range(len(q)):
                curr = q.popleft()
                tmp.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if lv % 2 == 0:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            lv += 1
        return res