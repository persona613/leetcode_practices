'''
Runtime: 62 ms, faster than 54.30% of Python3 online submissions 
Memory Usage: 14.6 MB, less than 92.39% of Python3 online submissions
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        cnode = None
        while curr:
            
            if curr.child:
                cnode = curr.child
                while cnode.next:
                    cnode = cnode.next
                cnode.next = curr.next
                if curr.next:
                    curr.next.prev = cnode
                curr.child.prev = curr
                curr.next = curr.child
                curr.child = None             
                    
            curr = curr.next
        return head