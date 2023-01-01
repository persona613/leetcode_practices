"""
79 ms runtime beats 76.80%
28 MB memory beats 10.77%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search_code(root, p, q):
            nonlocal ans
            code = 0
            if root is None:
                return code
            if root == p:
                code = 1
            elif root == q:
                code = 2
            
            code += search_code(root.left, p, q) \
                 +  search_code(root.right, p, q)
            if code == 3:
                ans.append(root)
            return code
        
        ans = []
        search_code(root, p, q)
        return ans[0]
        
        
            