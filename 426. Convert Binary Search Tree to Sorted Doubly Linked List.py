"""
41 ms runtime beats 30.06%
17.07 MB memory beats 84.93%
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
                
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            bag.append(node)
            traverse(node.right)
        
        if not root: return None
        bag = []
        traverse(root)
        head = bag[0]
        # left -> pre, right -> suf
        head.left = bag[-1]
        while bag:
            curr = bag.pop()
            if bag:
                curr.left = bag[-1]
            curr.right = head
            head = curr
        return head