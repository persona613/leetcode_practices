# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 208 / 208 test cases passed.
# Status: Accepted
# Runtime: 52 ms 65.52%
# Memory Usage: 14 MB 0%


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        tail = None

        if list1 == None:
            if list2 == None:
                return None
            else:
                return list2
        
        elif list2 == None:
            return list1
        
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                if head == None:
                    head = ListNode(list1.val)
                    tail = head
                else:
                    tail.next = ListNode(list1.val)
                    tail = tail.next
                    
                list1 = list1.next
                               
            else:
                if head == None:
                    head = ListNode(list2.val)
                    tail = head
                else:
                    tail.next = ListNode(list2.val)
                    tail = tail.next
                
                list2 = list2.next
            
        if list1 == None:
            tail.next = list2
        else:
            tail.next = list1
            
        return head
    
