"""
916 ms runtime beats 47.52%
65.39 MB memory beats 92.20%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        stk = []
        left = root
        while stk or left:
            if not left:
                curr = stk.pop()
                arr.append(curr.val)
                if curr.right:
                    left = curr.right
            else:
                stk.append(left)
                left = left.left
        # print(arr)

        n = len(arr)
        res = []
        for q in queries:
            i = bisect.bisect_left(arr, q)
            if i == n:
                res.append([arr[i - 1], -1])
            elif arr[i] == q:
                res.append([q, q])
            elif i == 0:
                res.append([-1, arr[i]])
            else:
                res.append([arr[i - 1], arr[i]])
        return res