"""
218 ms runtime beats 87.95%
20.41 MB memory beats 23.94%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(node):
            if not node:
                return 0            
            carry = dfs(node.next)
            double = node.val * 2 + carry
            node.val = double % 10
            return double // 10
        
        dummy = ListNode(0, head)
        dfs(dummy)
        return dummy if dummy.val else dummy.next