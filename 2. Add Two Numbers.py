'''
Runtime: 86 ms, faster than 75.35% of Python3 online submissions 
Memory Usage: 13.8 MB, less than 86.35% of Python3 online submissions
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        array1 = []
        array2 = []
        while l1:
            array1.append(l1.val)
            l1 = l1.next
        while l2:
            array2.append(l2.val)
            l2 = l2.next
            
        num1 = ''.join([str(array1[i]) for i in range(len(array1)-1, -1, -1)])
        num2 = ''.join([str(array2[i]) for i in range(len(array2)-1, -1, -1)])
        ans = int(num1) + int(num2)
        anslist = list(str(ans))
                       
        dummy = ListNode()
        cur = dummy
        for i in range(-1, -len(anslist)-1, -1):
            node = ListNode(anslist[i])
            cur.next = node
            cur = cur.next
        return dummy.next