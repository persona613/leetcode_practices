"""
39 ms runtime beats 53.65%
17.51 MB memory beats 5.04%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None: return head
        
        # ll = left's left, rr = right's right
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        prev = None
        idx = 0

        # find left's left node
        while idx < left - 1:
            curr = curr.next
            idx += 1
        ll = curr
        curr = curr.next
        idx += 1
        l = curr # mark left node
        while idx < right + 1:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            idx += 1
        # rr = curr
        # r = prev
        # connect list
        ll.next = prev
        l.next = curr
        return head if left != 1 else dummy.next
