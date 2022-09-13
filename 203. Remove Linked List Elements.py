'''
Runtime: 150 ms, faster than 7.24% of Python3 online submissions 
Memory Usage: 17.9 MB, less than 38.81% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        while head.val == val:
            head = head.next
            if not head:
                return head
        
        prev = head    
        cur = head.next        
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
                continue
            prev = cur
            cur = cur.next
            
        return head
            