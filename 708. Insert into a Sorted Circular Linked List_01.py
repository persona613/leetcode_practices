"""
Wrong Answer
37 / 111 testcases passed
submitted at Apr 25, 2024 11:17

Editorial
Input
[1,3,5]
6

Use Testcase
Output
[1,3,6,5]
Expected
[1,3,5,6]
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
            if curr.val <= insertVal:
                th = curr
                middle = True
                break
            if curr.val > curr.next.val:
                # find true tail
                th = curr
            curr = curr.next
        
        if middle == False and head.val <= insertVal:
            # insert after head
            th = head
        nxt = th.next
        th.next = Node(insertVal)
        th.next.next = nxt
        return head