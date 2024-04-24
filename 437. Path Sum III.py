"""
295 ms runtime beats 34.93%
16.94 MB memory beats 87.54%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def bfs(node):
            nonlocal ans
            q = deque([(node, 0)])
            while q:
                curr, tsum = q.popleft()
                tsum += curr.val
                if tsum == targetSum:
                    ans += 1
                if curr.left:
                    q.append((curr.left, tsum))
                if curr.right:
                    q.append((curr.right, tsum))

        def dfs(node):
            if not node: return

            bfs(node)
            dfs(node.left)
            dfs(node.right)

        ans = 0
        dfs(root)
        return ans