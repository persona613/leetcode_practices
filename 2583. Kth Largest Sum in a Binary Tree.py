"""
60 ms runtime beats 98.90%
52.77 MB memory beats 17.87%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelsum = []
        q = deque([root])
        while q:
            currsum = 0
            for _ in range(len(q)):
                node = q.popleft()
                currsum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelsum.append(currsum)
        if len(levelsum) >= k:
            return sorted(levelsum, reverse = True)[k - 1]
        else:
            return -1
