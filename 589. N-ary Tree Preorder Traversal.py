"""
43 ms runtime beats 98.54%
16.3 MB memory beats 13.8%
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            for o in node.children:
                dfs(o)
        
        res = []
        dfs(root)
        return res