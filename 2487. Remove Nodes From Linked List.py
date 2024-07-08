"""
419 ms runtime beats 58.67%
63.60 MB memory beats 5.03%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(node):
            if not node.next:
                return False, node.val
            
            remove_next, right_val = dfs(node.next)
            if remove_next == True:
                node.next = node.next.next

            if right_val > node.val:
                return True, right_val
            return False, node.val
        
        dummy = ListNode(inf, head)
        dfs(dummy)
        return dummy.next