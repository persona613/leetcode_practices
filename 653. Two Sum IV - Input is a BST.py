"""
94 ms runtime beats 47.87%
18.8 MB memory beats 69.96%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dic = defaultdict(set)
        q = deque([root])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if curr.val not in dic[curr.val//1000]:
                    m = k - curr.val
                    dic[m//1000].add(m)
                else:
                    return True
        return False