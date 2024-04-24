'''
Runtime: 289 ms, faster than 61.45% of Python3 online submissions 
Memory Usage: 32.08 MB, less than 70.18% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def pre_half_end(node):
            fast = slow = node
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(node):
            pre = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = pre
                pre = curr
                curr = nxt
            return pre
        
        pre_end = pre_half_end(head)
        nxt_start = reverse(pre_end.next)
        i = head
        j = nxt_start
        while i and j:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next

        pre_end.next = reverse(nxt_start)
        return True