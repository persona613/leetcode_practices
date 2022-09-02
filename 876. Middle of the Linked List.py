
'''
Runtime: 58 ms, faster than 22.60% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.7 MB, less than 95.57% of Python3 online submissions for Middle of the Linked List.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next
        offset = length // 2
        current = head
        for i in range(offset):
            current = current.next
        return current