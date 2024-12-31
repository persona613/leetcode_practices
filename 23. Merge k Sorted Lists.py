"""
79 ms runtime beats 53.82%
20.02 MB memory beats 8.21%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # min heap
        q = []
        # counter for heap can not sort by ListNode
        counter = 0
        for head in lists:
            if head:
                heapq.heappush(q, (head.val, counter, head))
                counter += 1

        tail = dummy = ListNode()
        while q:
            _, _, node = heapq.heappop(q)
            next_node = node.next
            node.next = None
            tail.next = node
            tail = tail.next
            if next_node:
                heapq.heappush(q, (next_node.val, counter, next_node))
                counter += 1
        return dummy.next