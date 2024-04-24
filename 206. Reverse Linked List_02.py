'''
Runtime: 41 ms, faster than 77.21% of Python3 online submissions 
Memory Usage: 20.5 MB, less than 8.32% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pivot = None
        def reverse(pivot, head):
            if not head:
                return pivot
            curr = head
            head, curr.next, pivot = head.next, pivot, curr
            return reverse(pivot, head)
        
        return reverse(pivot, head)
            