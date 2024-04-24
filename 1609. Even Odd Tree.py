"""
234 ms runtime beats 51.58%
51.37 MB memory beats 14.40%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, level):
            if not node:
                return True

            if node.val % 2 == level % 2:
                return False
            if level == len(prev):
                prev.append(0)
            if prev[level] != 0:
                if (level % 2 == 0 and node.val <= prev[level]) or \
                        (level % 2 == 1 and node.val >= prev[level]):
                    return False
            
            prev[level] = node.val
            return dfs(node.left, level + 1) and dfs(node.right, level + 1)

        prev = []
        return dfs(root, 0)