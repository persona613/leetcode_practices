'''
Runtime: 112 ms, faster than 16.15% of Python3 online submissions 
Memory Usage: 17.7 MB, less than 30.75% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        fast = head
        slow = head
        
        while True:
            if fast.next == None:
                return False
            if fast.next.next == None:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            