"""
34 ms runtime beats 95.62%
16.96 MB memory beats 29.48%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        d = {0: dummy}
        presum = 0
        stk = []
        while curr:
            presum += curr.val
            if presum in d:
                # del nodes
                pre = d[presum]
                pre.next = curr.next
                # del presum record
                while stk and stk[-1] != presum:
                    del d[stk.pop()]
            else:
                d[presum] = curr
                stk.append(presum)
            curr = curr.next
        return dummy.next