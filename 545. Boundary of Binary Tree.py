"""
48 ms runtime beats 19.76%
17.72 MB memory beats 25.20%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return [root.val]
        
        def left_bound(node, path):
            if not node:
                return path
            if not node.left and not node.right:
                return path
            path.append(node.val)
            if node.left:
                return left_bound(node.left, path)
            return left_bound(node.right, path)

        def right_bound(node, path):
            if not node:
                return path
            if not node.left and not node.right:
                return path
            path.append(node.val)
            if node.right:
                return right_bound(node.right, path)
            return right_bound(node.left, path)

        def child(node, path):
            if not node:
                return path
            if not node.left and not node.right:
                path.append(node.val)
                return path
            child(node.left, path)
            child(node.right, path)
            return path

        return [root.val] + left_bound(root.left, []) \
                + child(root, []) + right_bound(root.right, [])[::-1]