"""
48 ms runtime beats 89.98%
25.17 MB memory beats 5.76%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def dfs(node):
            if not node: return
            dfs(node.next)
            if self.finish: return
            if self.curr == node or self.curr.next == node:
                node.next = None
                self.finish = True
                return
            node.next = self.curr.next
            self.curr.next = node
            self.curr = node.next

        self.curr = head
        self.finish = False
        dfs(self.curr)