"""
26 ms runtime beats 98.48%
16.81 MB memory beats 63.91%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ln = 0
        curr = head
        while curr:
            ln += 1
            curr = curr.next
        
        size, extra = divmod(ln, k)
        res = [None] * k
        pre = None
        curr = head
        i = 0
        while i < extra and curr:
            # part's start
            res[i] = curr
            j = 0
            while curr and j < size + 1:
                pre = curr
                curr = curr.next
                j += 1
            # part's end
            pre.next = None
            i += 1

        while i < k and curr:
            res[i] = curr
            j = 0
            while curr and j < size:
                pre = curr
                curr = curr.next
                j += 1
            pre.next = None
            i += 1
        return res