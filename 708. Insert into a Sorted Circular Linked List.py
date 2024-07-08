"""
44 ms runtime beats 17.73%
17.22 MB memory beats 38.47%
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head        

        curr = head.next
        # the insert point
        th = head
        # find insert point at middle
        middle = False
        while curr != head:
            # find insert position
            if curr.val <= insertVal and insertVal <= curr.next.val:
                th = curr
                middle = True
                break
            if curr.val > curr.next.val:
                # find true tail
                th = curr
            curr = curr.next
        
        if middle == False and head.val <= insertVal \
                and insertVal <= head.next.val:
            # insert after head
            th = head
        nxt = th.next
        th.next = Node(insertVal)
        th.next.next = nxt
        return head