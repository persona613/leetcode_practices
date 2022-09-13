'''
Runtime: 98 ms, faster than 0% of Python3 online submissions 
Memory Usage: 15.6 MB, less than 28.36% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        target = None
        if not head:
            return head
        while head.next:
            target = head.next
            head.next = head.next.next
            target.next = start
            start = target
        # head = start
        return start