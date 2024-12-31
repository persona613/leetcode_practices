"""
671 ms runtime beats 57.10%
55.12 MB memory beats 52.61%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dr = ci = cj = 0
        di, dj = dirs[dr]
        curr = head
        while curr:
            res[ci][cj] = curr.val
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < m and 0 <= nj < n and res[ni][nj] == -1:
                ci = ni
                cj = nj
            else:
                dr = (dr + 1) % 4
                di, dj = dirs[dr]
                ci += di
                cj += dj
            curr = curr.next
        return res