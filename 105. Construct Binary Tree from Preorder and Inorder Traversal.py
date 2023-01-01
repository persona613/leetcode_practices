"""
57 ms runtime beats 97.11%
19 MB memory beats 77.96%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # [lo, hi](not include hi) for find mid-node index 
        def solve(lo, hi):
            nonlocal rootindex
            if lo == hi:
                return
            root = TreeNode(preorder[rootindex])
            mid = inorder_dict[preorder[rootindex]]
            rootindex += 1
            
            root.left = solve(lo, mid)
            root.right = solve(mid+1, hi)
            
            return root
        
        inorder_dict = {v:i for i,v in enumerate(inorder)}
        rootindex = 0
        
        return solve(0, len(inorder))