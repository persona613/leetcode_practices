"""
41 ms runtime beats 53.78%
16.4 MB memory beats 22.45%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans*2 + head.val
            head = head.next
        return ans