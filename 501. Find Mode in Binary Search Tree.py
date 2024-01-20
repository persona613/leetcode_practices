"""
46 ms runtime beats 95.48%
20.71 MB memory beats 36.54%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        def dfs(node):
            if not node: return
            dic[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        mx = max(dic.values())
        res = []
        for k in dic:
            if dic[k] == mx:
                res.append(k)
        return res