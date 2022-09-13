'''
Runtime: 68 ms, faster than 29.28% of Python3 online submissions 
Memory Usage: 14 MB, less than 0% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        curr1 = list1
        curr2 = list2
        dummy = ListNode()
        newnode = dummy
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                newnode.next = curr1
                newnode = newnode.next
                curr1 = curr1.next
                continue
            if curr2.val <= curr1.val:
                newnode.next = curr2
                newnode = newnode.next
                curr2 = curr2.next
                continue
        if not curr1:
            newnode.next = curr2
            return dummy.next
        elif not curr2:
            newnode.next = curr1
            return dummy.next