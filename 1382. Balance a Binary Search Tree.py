"""
182 ms runtime beats 94.68%
20.21 MB memory beats 89.29%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)

        def bst_tree(l, r, arr):
            if l > r:
                return
            mid = (l + r) // 2
            new_root = arr[mid]
            new_root.left = bst_tree(l, mid - 1, arr)
            new_root.right = bst_tree(mid + 1, r, arr)
            return new_root

        nodes = []
        inorder(root)
        return bst_tree(0, len(nodes) - 1, nodes)