"""
37 ms runtime beats 58.80%
16.42 MB memory beats 81.83%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
            
        curr = head
        less = ltail = ListNode()
        bigg = btail = ListNode()
        while curr:
            if curr.val < x:
                ltail.next = curr
                ltail = ltail.next
                curr = curr.next
                # ltail.next = None
            else:
                btail.next = curr
                btail = btail.next
                curr = curr.next
                # btail.next = None
        ltail.next = bigg.next
        btail.next = None
        return less.next
        