"""
1353 ms runtime beats 51.74%
16.6 MB memory beats 44.75%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr.next:
            before_curr = curr
            curr = curr.next
            start = head
            before_st = None
            while start != curr:
                               
                if curr.val >= start.val:
                    before_st = start
                    start = start.next
                elif curr.val < start.val:
                    # remove curr-node
                    before_curr.next = curr.next
                    # insert curr-node forward
                    if before_st:
                        before_st.next = curr
                        curr.next = start
                    else:
                        curr.next = start
                        head = curr
                    # update curr
                    curr = before_curr
                    break 
        return head