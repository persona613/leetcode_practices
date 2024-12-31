"""
39 ms runtime beats 99.61%
16.2 MB memory beats 45.67%
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def dfs(node):
            if not node:
                return
            for o in node.children:
                dfs(o)
            res.append(node.val)
            
        
        res = []
        dfs(root)
        return res