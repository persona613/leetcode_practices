"""
1586 ms runtime beats 46.13%
25.81 MB memory beats 67.68%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic = dict()
        indegree = set()
        for parent, child, isleft in descriptions:
            par = dic.setdefault(parent, TreeNode(parent))
            if isleft:
                par.left = dic.setdefault(child, TreeNode(child))
            else:
                par.right = dic.setdefault(child, TreeNode(child))
            indegree.add(child)
        for key in dic:
            if key in indegree:
                indegree.remove(key)
            else:
                return dic[key]
        return dic[indegree.pop()]