"""
39 ms runtime beats 97.70%
16.1 MB memory beats 46.69%
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node, dp):
            nonlocal ans
            if not node:
                return
            if not node.children:
                ans = max(ans, dp)
                return
            for o in node.children:
                dfs(o, dp+1)
        
        ans = 0
        dfs(root, 1)
        return ans