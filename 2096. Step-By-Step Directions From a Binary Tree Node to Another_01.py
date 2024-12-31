"""
Wrong Answer
119 / 332 testcases passed

Editorial
Input
root =
[5,8,3,1,null,4,7,6,null,null,null,null,null,null,2]
startValue =
4
destValue =
3

Use Testcase
Output
"UUR"
Expected
"U"
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

        tpath = tpath[::-1]
        i = j = 0
        while i < len(spath) and j < len(tpath):
            if spath[i] != tpath[j]:
                break
            i += 1
            j += 1
        spath = ["U"] * (len(spath) - i)
        spath.extend(tpath[j:])
        return "".join(spath)