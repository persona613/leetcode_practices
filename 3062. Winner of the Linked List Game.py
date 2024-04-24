"""
35 ms runtime beats 100%
16.55 MB memory beats 100%
Sorry, there are not enough accepted submissions to show data
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd = even = 0
        curr = head
        while curr:
            if curr.val > curr.next.val:
                even += 1
            else:
                odd += 1
            curr = curr.next.next
        if odd == even:
            return "Tie"
        return "Odd" if odd > even else "Even"