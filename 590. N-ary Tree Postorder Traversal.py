"""
43 ms runtime beats 73.64%
18.11 MB memory beats 77.39%
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
        if not root:
            return
        res = []
        stk = [(root, False)]
        while stk:
            curr, seen = stk.pop()
            if seen:
                res.append(curr.val)
            else:
                stk.append((curr, True))
                for node in reversed(curr.children):
                    stk.append((node, False))
        return res