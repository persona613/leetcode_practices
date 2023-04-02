"""
51 ms runtime beats 82.59%
18.1 MB memory beats 40.33%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(node):
            nonlocal cnt, ans
            if not node:
                return  
            if inorder(node.left):         
                return True
            cnt += 1
            if cnt == k:
                ans = node.val
                return True
            if inorder(node.right):
                return True
        cnt = 0 
        ans = None   
        inorder(root)
        return ans