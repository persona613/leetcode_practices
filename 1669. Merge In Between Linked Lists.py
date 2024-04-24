"""
211 ms runtime beats 14.90%
21.12 MB memory beats 31.60%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        d = b - a + 2
        prea = surb = list1
        for _ in range(d):
            surb = surb.next
        for _ in range(a - 1):
            prea = prea.next
            surb = surb.next
        tail = list2
        while tail.next:
            tail = tail.next
        prea.next = list2
        tail.next = surb
        return list1