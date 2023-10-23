
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
479 ms runtime beats 49.30%
26 MB memory beats 73.61%
"""
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # road:0=left, 1=right
        def dfs(head, target, road):
            if not head: return
            if head == target:
                path.append(road)
                return True
            l = dfs(head.left, target, 0)
            if l: 
                path.append(road)
                return True
            r = dfs(head.right, target, 1)
            if r: 
                path.append(road)
                return True

        path = []
        dfs(original, target, None)
        path.pop()
        curr = cloned
        for p in path[::-1]:
            if p == 0:
                curr = curr.left
            else:
                curr = curr.right
        return curr
        