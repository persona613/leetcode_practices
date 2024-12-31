"""
71 ms runtime beats 54.46%
19.65 MB memory beats 36.27%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            while b > 0:
                a, b = b, a % b
            return a
        
        curr = head
        nxt = head.next
        while nxt:
            d = gcd(curr.val, nxt.val)
            new_node = ListNode(d, nxt)
            curr.next = new_node

            curr = nxt
            nxt = curr.next
        return head