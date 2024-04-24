"""
33 ms runtime beats 73.14%
16.38 MB memory beats 99.36%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        cnt = 0
        curr = head
        while curr:
            curr = curr.next
            cnt += 1
        ans = head
        for _ in range(cnt // 2):
            ans = ans.next
        return ans        