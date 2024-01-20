"""
399 ms runtime beats 97.08%
41.15 MB memory beats 99.49%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head
        for _ in range(k-1):
            fast = fast.next
        node = fast
        while fast.next:
            fast = fast.next
            slow = slow.next
        node.val, slow.val = slow.val, node.val
        return head
