"""
58 ms runtime beats 73.98%
15.3 MB memory beats 92.54%
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def search_next(root):
            curr = root.next
            while curr:
                if curr.left:
                    return curr.left
                elif curr.right:
                    return curr.right
                curr = curr.next
            return curr
        
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = search_next(root)
        if root.right:
            root.right.next = search_next(root)
            
        self.connect(root.right)
        self.connect(root.left)
        return root