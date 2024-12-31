"""
38 ms runtime beats 42.44%
16.44 MB memory beats 64.29%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        def dfs(node):
            if not node:
                return 1

            if dfs(node.next):
                sm = node.val + 1
                node.val = sm % 10
                return sm // 10

        dummy = ListNode(0, head)
        dfs(dummy)
        return dummy if dummy.val else head