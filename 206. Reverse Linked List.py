'''
Runtime: 36 ms, faster than 67.15% of Python3 online submissions 
Memory Usage: 17.70 MB, less than 77.25% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # l = None
        # r = head
        # while r:
        #     r = r.next
        #     head.next = l
        #     l = head
        #     head = r
        # return l

        def dfs(l, head):
            if not head:
                return l
            r = head.next
            head.next = l
            l = head
            head = r
            return dfs(l, head)
        
        return dfs(None, head)

            