"""
312 ms runtime beats 100%
43.18 MB memory beats 98.67%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, bm):
            if not node: return

            bm ^= 1 << node.val
            if not node.left and not node.right:
                if int.bit_count(bm) < 2:
                    self.ans += 1
                return
            
            dfs(node.left, bm)
            dfs(node.right, bm)
        
        dfs(root, 0)
        return self.ans            
