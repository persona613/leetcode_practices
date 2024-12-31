"""
55 ms runtime beats 61.34%
16.72 MB memory beats 5.81%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1 = []
        curr = l1
        while curr:
            stk1.append(curr.val)
            curr = curr.next
        stk2 = []
        curr = l2
        while curr:
            stk2.append(curr.val)
            curr = curr.next
        
        carry = 0
        pre = None
        while stk1 or stk2:
            sm = carry
            sm += stk1.pop() if stk1 else 0
            sm += stk2.pop() if stk2 else 0

            carry = sm // 10
            curr = ListNode(sm % 10, pre)
            pre = curr

        if carry:
            curr = ListNode(carry, pre)
        return curr