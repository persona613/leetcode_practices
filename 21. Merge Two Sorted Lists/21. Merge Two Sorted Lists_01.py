# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        tail = None
        
        
        if list1 == None:
            if list2 == None:
                return None
            else:
                return list2
        
        while list2 != None:
            if list1.val >= list2.val:
                if head == None:
                    head = ListNode(list2.val)
                    tail = head
                else:
                    tail.next = ListNode(list2.val)
                    tail = tail.next         

                tail.next = list1
                list1 = head
                head = None
                tail = None

                list2 = list2.next
                continue


            elif list1.val < list2.val:
                if head == None:
                    head = ListNode(list1.val)
                    tail = head
                else:
                    tail.next = ListNode(list1.val)
                    tail = tail.next
                    
                list1 = list1.next
                if list1 == None:
                    tail.next = ListNode(list2.val)
                    tail = tail.next
                    list1 = head
                    list2 = list2.next

        return list1
    
