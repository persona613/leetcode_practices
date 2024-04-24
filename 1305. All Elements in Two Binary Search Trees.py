"""
2251 ms runtime beats 5.04%
23.86 MB memory beats 25.17%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def gen(node):
            if not node:
                return
            yield from gen(node.left)
            yield node.val
            yield from gen(node.right)
        
        f1 = gen(root1)
        f2 = gen(root2)
        a = next(f1, None)
        b = next(f2, None)
        res = []
        while a != None and b != None:
            if a <= b:
                res.append(a)
                a = next(f1, None)
            else:
                res.append(b)
                b = next(f2, None)
        if a == None:
            while b != None:
                res.append(b)
                b = next(f2, None)
        if b == None:
            while a != None:
                res.append(a)
                a = next(f1, None)
        return res
