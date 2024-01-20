"""
351 ms runtime beats 99.14%
45.15 MB memory beats 84.12%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # find first mid node
        fast = slow = head
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # reverse right half linked list
        rev = reverse(slow.next)
        slow.next = rev

        left = head
        right = rev
        ans = 0
        while right:
            t = left.val + right.val
            if t > ans:
                ans = t
            left = left.next
            right = right.next
        return ans
