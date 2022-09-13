'''
Runtime: 88 ms, faster than 15.2% of Python3 online submissions 
Memory Usage: 16.6 MB, less than 77.79% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        
        
        odddummy = ListNode()
        evendummy = ListNode()
        oddtail = odddummy        
        eventail = evendummy
        cur = head
        i = 1
        while cur:
            if i % 2 == 1:
                tmp = cur.next
                cur.next = None
                oddtail.next = cur
                oddtail = oddtail.next
            else:
                tmp = cur.next
                cur.next = None
                eventail.next = cur
                eventail = eventail.next
            cur = tmp
            i += 1
        oddtail.next = evendummy.next
        return odddummy.next