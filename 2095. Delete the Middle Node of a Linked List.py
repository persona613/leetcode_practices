"""
627 ms runtime beats 97.66%
51.38 MB memory beats 98.74%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        dummy = ListNode()
        dummy.next = head
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            dummy = dummy.next
        dummy.next = slow.next
        return head