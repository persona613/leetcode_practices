"""
785 ms runtime beats 96.17%
44.35 MB memory beats 95.74%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return head
        def reverse(A, B, C, k):
            curr = B
            prev = None
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            A.next = C
            B.next = D
        A = None
        B = C = head
        D = head.next
        k = 1
        while D:
            if k % 2 == 0:
                # reverse k gruop
                reverse(A, B, C, k)
                # reset A,B to next group line
                A = B
                C = B
                B = D
            else:
                A = C
                B = D
            # move C,D to next group line
            k += 1
            moves = 0
            while D and moves < k:
                D = D.next
                C = C.next
                moves += 1
        if moves % 2 == 0:
            reverse(A, B, C, moves)
        return head
            