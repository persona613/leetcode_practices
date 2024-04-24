"""
43 ms runtime beats 78.75%
17.74 MB memory beats 73.75%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        d = 1
        q = deque([root])
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                if d == depth - 1:
                    new_left = TreeNode(val)
                    new_right = TreeNode(val)
                    new_left.left = curr.left
                    new_right.right = curr.right
                    curr.left = new_left
                    curr.right = new_right
                else:
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            d += 1
        return root