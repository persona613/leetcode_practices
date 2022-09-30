'''
Runtime: 45 ms, faster than 83.78% of Python3 online submissions 
Memory Usage: 13.9 MB, less than 79.08% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        dic = {}
        new = []
        curr = head
        end = None
        while curr:
            new.append(curr)
            if curr.next == None:
                end = curr
            curr = curr.next
        n = len(new)
        for i in range(n):
            pos = (i+k)%n
            dic[pos] = new[i]
        for j in range(n):
            new[j] = dic[j]
        end.next = head
        new[-1].next = None
        return new[0]