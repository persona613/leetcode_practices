"""
54 ms runtime beats 51.27%
20.34 MB memory beats 50.61%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        def inorder(node, target):
            nonlocal pre, ans
            if ans:
                return

            if node.left:            
                inorder(node.left, target)
            if pre and pre == target:
                ans = node
            pre = node
            if node.right:
                inorder(node.right, target)

        pre = None
        ans = None
        inorder(root, p)
        return ans