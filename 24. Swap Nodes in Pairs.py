"""
38 ms runtime beats 71.71%
14 MB memory beats 18.64%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tmp = head.next
        head.next = self.swapPairs(head.next.next)       
        tmp.next = head
        head = tmp   
        
        return head