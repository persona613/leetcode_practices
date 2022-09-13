'''
Runtime: 45 ms, faster than 69.41% of Python3 online submissions 
Memory Usage: 13.9 MB, less than 0% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = head
        j = head
        cnt = 0
        prev = head
        # sz = 1
        while head.next == None and n == 1:
            head = head.next
            return head
        while cnt != n:
            j = j.next
            cnt += 1
        # n = remnove head node
        if j == None:
            head = head.next
            return head
        while j:
            j = j.next
            prev = i
            i = i.next
        prev.next = i.next
        return head
            