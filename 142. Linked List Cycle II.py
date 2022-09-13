'''
Runtime: 99 ms, faster than 25.1% of Python3 online submissions 
Memory Usage: 18 MB, less than 0% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeset = set()
        cur = head
        while cur != None:
            if cur in nodeset:
                return cur
            else:
                nodeset.add(cur)
            cur = cur.next
        return None