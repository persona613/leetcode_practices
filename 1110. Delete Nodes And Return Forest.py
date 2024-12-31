"""
62 ms runtime beats 21.37%
16.96 MB memory beats 61.78%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # isdele: for parent-node is delete
        def dfs(node, par_dele):
            if not node:
                return
            if node.val in to_delete:
                dfs(node.left, True)
                dfs(node.right, True)
                # node.left = None
                # node.right = None
                return False

            l = dfs(node.left, False)
            r = dfs(node.right, False)
            
            # remove delete-child-node
            if not l:
                node.left = None
            if not r:
                node.right = None

            # if parent node is dele, add root
            if par_dele:
                res.append(node)
            return True

        res = []
        dfs(root, True)
        return res