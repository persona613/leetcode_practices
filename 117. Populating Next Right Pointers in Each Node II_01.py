"""
Submission Result: Wrong Answer 
Input:
[1,2,3,4,5,null,6,7,null,null,null,null,8]
Output:
[1,#,2,3,#,4,5,6,#,7,#]
Expected:
[1,#,2,3,#,4,5,6,#,7,8,#]
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
            if root.next is None:
                return None
            if root.next.left:
                return root.next.left
            elif root.next.right:
                return root.next.right
            else:
                return None
                
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