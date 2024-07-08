"""
489 ms runtime beats 48.58%
46.02 MB memory beats 64.54%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # count dict
        curr = head
        cnt = defaultdict(int)
        while curr:
            cnt[curr.val] += 1
            curr = curr.next
        
        dummy = ListNode(0, head)
        pre = dummy
        curr = head
        while curr:
            if cnt[curr.val] > 1:
                pre.next = curr.next
            else:
                pre = pre.next
                
            curr = curr.next
        return dummy.next