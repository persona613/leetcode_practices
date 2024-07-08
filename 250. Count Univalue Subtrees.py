"""
37 ms runtime beats 61.60%
16.61 MB memory beats 39.44%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node.left and not node.right:
                return True, 1

            if node.left and node.right:
                lstate, lcnt = dfs(node.left)
                rstate, rcnt = dfs(node.right)
                if lstate and rstate and node.val == node.left.val \
                        and node.val == node.right.val:
                    return True, lcnt + rcnt + 1
                else:
                    return False, lcnt + rcnt
            elif node.left:
                lstate, lcnt = dfs(node.left)
                if lstate and node.val == node.left.val:
                    return True, lcnt + 1
                else:
                    return False, lcnt
            else:
                rstate, rcnt = dfs(node.right)
                if rstate and node.val == node.right.val:
                    return True, rcnt + 1
                else:
                    return False, rcnt

        if not root: return 0
        state, cnt = dfs(root)
        return cnt