"""
236 ms runtime beats 93.96%
53.93 MB memory beats 29.36%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def search(node, target, path):
            if not node:
                return
            if node.val == target:
                return True
            l = search(node.left, target, path)
            if l:
                path.append("L")
                return True
            r = search(node.right, target, path)
            if r:
                path.append("R")
                return True
        
        spath = []
        search(root, startValue, spath)
        tpath = []
        search(root, destValue, tpath)

        # trim path: root to LCA
        i = len(spath) - 1
        j = len(tpath) - 1
        while i >= 0 and j >= 0:
            if spath[i] != tpath[j]:
                break
            i -= 1
            j -= 1
        spath = ["U"] * (i + 1)
        spath.extend(tpath[:j + 1][::-1])
        return "".join(spath)