"""
56 ms runtime beats 97.24%
18.9 MB memory beats 86.35%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
                
        # [start,end] for inorder list to find mid-node index
        def solve(start, end):            
            nonlocal rootindex
            if start > end:
                return
            root = TreeNode(postorder[rootindex])
            mid = inorder_dict[postorder[rootindex]]
            rootindex -= 1
            
            root.right = solve(mid+1, end)
            root.left = solve(start, mid-1)            
            return root
        
        inorder_dict = {v:i for i,v in enumerate(inorder)}
        rootindex = -1
        return solve(0, len(inorder)-1)