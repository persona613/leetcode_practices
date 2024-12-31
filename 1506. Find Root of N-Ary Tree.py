"""
99 ms runtime beats 29.93%
26.69 MB memory beats 10.22%
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
            if type(node.val) is int:
                node.val = str(node.val)
                for chi in node.children:
                    dfs(chi)

        # root indgree = 0
        # seen children_node set to negtive value
        for node in tree:
            if type(node.val) is int:
                for chi in node.children:
                    dfs(chi)
        res = None
        for node in tree:
            if type(node.val) is int:
                res = node
            # else:
                # node.val = int(node.val)
        return res