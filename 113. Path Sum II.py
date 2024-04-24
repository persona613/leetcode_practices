"""
41 ms runtime beats 75.78%
21.18 MB memory beats 30.60%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, arr, asum):
            if not node: return
            if not node.left and not node.right:
                if asum + node.val == targetSum:
                    arr.append(node.val)
                    res.append(arr)
                    return
            dfs(node.left, arr + [node.val], asum + node.val)
            dfs(node.right, arr + [node.val], asum + node.val)
        res = []
        dfs(root, [], 0)
        return res