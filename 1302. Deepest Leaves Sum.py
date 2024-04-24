"""
133 ms runtime beats 68.38%
19.45 MB memory beats 100%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def depth(node):
            if not node:
                return -1
            return max(depth(node.left), depth(node.right)) + 1
        
        k = depth(root)
        q = deque([root])
        ans = lv = 0
        while q:
            if lv == k:
                break
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            lv += 1
        while q:
            ans += q.popleft().val
        return ans