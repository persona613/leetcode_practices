"""
40 ms runtime beats 76.25%
17.69 MB memory beats 88.96%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, arr):
            nonlocal res
            if not node:
                return
            
            arr.appendleft(chr(node.val + 97))
            if not node.left and not node.right:
                s = "".join(arr)
                if not res or s < res:
                    res = s
                arr.popleft()
                return
            dfs(node.left, arr)
            dfs(node.right, arr)
            arr.popleft()
        
        res = ""
        dfs(root, deque())
        return res