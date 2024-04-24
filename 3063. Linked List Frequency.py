"""
466 ms runtime beats 99.12%
37.45 MB memory beats 98.25%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = defaultdict(int)
        curr = head
        while curr:
            f[curr.val] += 1
            curr = curr.next
        dummy = curr = ListNode()
        for v in f.values():
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next