"""
220 ms runtime beats 98.21%
59.76 MB memory beats 58.97%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        # return height of curr-node
        def dfs(node, level):
            if not node:
                return -1
            # prevent out of index range
            if level >= len(max2h):
                max2h.append([-1, -1])
            
            ld = dfs(node.left, level + 1)
            rd = dfs(node.right, level + 1)
            h = max(ld, rd) + 1
            dic[node.val] = (level, h)

            if h > max2h[level][0]:
                max2h[level][1] = max2h[level][0]
                max2h[level][0] = h
            elif h > max2h[level][1]:
                max2h[level][1] = h
            return h

        # two max height of subtree at each level
        max2h = []
        # node: (level, height)
        dic = dict()
        # traverse tree
        dfs(root, 0)

        res = []
        for q in queries:
            lv, h = dic[q]
            if h == max2h[lv][0]:
                res.append(lv + max2h[lv][1])
            else:
                res.append(lv + max2h[lv][0])
        return res