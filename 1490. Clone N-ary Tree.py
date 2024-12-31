"""
51 ms runtime beats 92.08%
19.75 MB memory beats 63.33%
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        curr = Node(root.val, [])
        for ch in root.children:
            curr.children.append(self.cloneTree(ch))
        return curr