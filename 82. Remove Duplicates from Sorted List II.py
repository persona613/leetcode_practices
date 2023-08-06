"""
52 ms runtime beats 82.87%
16.3 MB memory beats 89.99%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("inf"), head)
        curr = head
        prev = dummy
        t = False # remove-switch
        while curr and curr.next:
            while curr.val == curr.next.val:
                t = True
                if not curr.next.next:
                    prev.next = None
                    return dummy.next
                curr.next = curr.next.next
            if t:
                curr = curr.next
                prev.next = curr
                t = False
            else:
                prev = curr
                curr = curr.next
        return dummy.next