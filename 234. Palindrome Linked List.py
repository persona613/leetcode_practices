'''
Runtime: 868 ms, faster than 88.32% of Python3 online submissions 
Memory Usage: 46.7 MB, less than 37.54% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        while head == None:
            return False
        # while head.next == None:
        #     return True
        nodelist = []
        cur = head
        while cur:
            nodelist.append(cur.val)
            cur = cur.next
            
        # revlist = list(reversed(nodelist))
        revlist = nodelist[:]        
        revlist.reverse()
        # print(revlist)
        if nodelist == revlist:            
            return True
        else:
            return False