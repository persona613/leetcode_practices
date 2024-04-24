"""
Wrong Answer
30 / 35 testcases passed
Input
root =
[9,6,14,null,null,13,20,12]
queries =
[19,10,9,17,19,6,10,19,13,6]

Use Testcase
Output
[[14,20],[9,12],[9,9],[14,20],[14,20],[-1,6],[9,12],[14,20],[13,13],[-1,6]]
Expected
[[14,20],[9,12],[9,9],[14,20],[14,20],[6,6],[9,12],[14,20],[13,13],[6,6]]
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
            elif i == 0:
                res.append([-1, arr[i]])
            elif arr[i] == q:
                res.append([q, q])
            else:
                res.append([arr[i - 1], arr[i]])
        return res
