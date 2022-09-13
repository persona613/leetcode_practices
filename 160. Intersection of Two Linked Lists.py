'''
Runtime: 165 ms, faster than 93.08% of Python3 online submissions 
Memory Usage: 32.1 MB, less than 0% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeset = set()
        i = headA
        j = headB
        while i or j:
            if i in nodeset:
                return i
            if i:
                nodeset.add(i)
                i = i.next
            if j in nodeset:
                return j
            if j:
                nodeset.add(j)
                j = j.next
        return None
            
        