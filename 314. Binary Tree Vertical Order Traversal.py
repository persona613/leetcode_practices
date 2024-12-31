"""
34 ms runtime beats 78.17%
16.56 MB memory beats 28.71%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dic = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, col = q.popleft()
            dic[col].append(node.val)
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        mi = min(dic.keys())
        mx = max(dic.keys())
        res = []
        for i in range(mi, mx + 1):
            # array reference
            res.append(dic[i])
        return res