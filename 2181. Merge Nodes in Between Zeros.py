"""
726 ms runtime beats 92.67%
53.10 MB memory beats 95.19%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        fast = head.next
        sm = 0
        while fast:
            if fast.val == 0:
                # record at pointer.next
                pointer.next.val = sm
                pointer = pointer.next
                sm = 0
            else:
                sm += fast.val
            fast = fast.next
            
        pointer.next = None
        return head.next