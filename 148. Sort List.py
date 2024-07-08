"""
404 ms runtime beats 9.78%
31.74 MB memory beats 99.77%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        midnode = self.get_midnode(head)
        left = self.sortList(head)
        right = self.sortList(midnode)

        return self.merge(left, right)

    def get_midnode(self, head):
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        midnode = slow.next
        slow.next = None
        return midnode

    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
            
        if left:
            tail.next = left
        else:
            tail.next = right
        return dummy.next