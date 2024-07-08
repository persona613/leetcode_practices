"""
34 ms runtime beats 73.41%
16.50 MB memory beats 74.62%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def dfs(node, presum):
            if not node:
                return None, presum

            r_child, r_sum = dfs(node.right, presum)
            node.val += r_sum
            l_child, l_sum = dfs(node.left, node.val)
            return node, l_sum

        return dfs(root, 0)[0]