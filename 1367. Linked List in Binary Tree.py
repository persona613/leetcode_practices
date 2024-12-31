"""
88 ms runtime beats 20.77%
17.72 MB memory beats 26.12%
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False

            if head.val == root.val:
                return dfs(head.next, root.left) \
                    or dfs(head.next, root.right)
            return False

        if not root:
            return False

        if head.val == root.val:
            l = dfs(head.next, root.left)
            r = dfs(head.next, root.right)
            if l or r:
                return True

        return self.isSubPath(head, root.left) \
            or self.isSubPath(head, root.right)