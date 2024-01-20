'''
Runtime: 31 ms, faster than 98.26% of Python3 online submissions 
Memory Usage: 14 MB, less than 5.13% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        def takeone(list1, list2):
            nonlocal tail
            if not list1 and not list2:
                return
            if not list1:
                tail.next = list2
                list2 = list2.next
            elif not list2:
                tail.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            takeone(list1, list2)
        
        takeone(list1, list2)
        return dummy.next