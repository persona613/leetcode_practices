"""
176 ms runtime beats 95.80%
67.88 MB memory beats 42.31%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelsum = []
        children_sum = dict()
        q = deque([root])
        while q:
            currsum = 0
            for _ in range(len(q)):
                node = q.popleft()
                currsum += node.val

                # children sum
                chsum = 0
                if node.left:
                    q.append(node.left)
                    chsum += node.left.val
                if node.right:
                    q.append(node.right)
                    chsum += node.right.val
                children_sum[node] = chsum
            levelsum.append(currsum)

        root.val = 0
        q.append(root)
        # next depth
        d = 1
        while q:
            for _ in range(len(q)):
                parent = q.popleft()
                if parent.left:
                    parent.left.val = levelsum[d] - children_sum[parent]
                    q.append(parent.left)
                if parent.right:
                    parent.right.val = levelsum[d] - children_sum[parent]
                    q.append(parent.right)
            d += 1
        return root
        