"""
32 ms runtime beats 89.93%
17.19 MB memory beats 21.17%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr= []
        while head:
            arr.append(head)
            head = head.next
        return arr[len(arr)//2]