"""
Wrong Answer
20 / 24 testcases passed
submitted at May 03, 2024 14:13

Editorial
Input
[6,2,8,0,4,7,9,null,null,3,5]
2

Use Testcase
Output
4
Expected
3
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
            if not node:
                return

            ret = inorder(node.left, target)
            if ret:
                ans[0] = node
                return
            if node == target:
                if node.right:
                    ans[0] = node.right
                    return
                return True
            return inorder(node.right, target)

        ans = [None]
        inorder(root, p)
        return ans[0]