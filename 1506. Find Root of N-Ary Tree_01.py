"""
Wrong Answer
38 / 39 testcases passed
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':

        def dfs(node):
            if node.val < 0:
                return
            node.val *= -1
            for chi in node.children:
                dfs(chi)

        # root indgree = 0
        # seen children_node set to negtive value
        for node in tree:
            if node.val > 0:
                for chi in node.children:
                    dfs(chi)

        for node in tree:
            if node.val > 0:
                res = node
            else:
                node.val *= -1
        return res