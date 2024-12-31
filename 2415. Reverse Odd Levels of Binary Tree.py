"""
12 ms runtime beats 91.28%
23.13 MB memory beats 5.08%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(currlv, arr):
            if currlv % 2:
                i, j = 0, len(arr) - 1
                while i < j:
                    arr[i].val, arr[j].val = arr[j].val, arr[i].val
                    i += 1
                    j -= 1

            if not arr[0].left:
                return

            nxt_arr = []
            for node in arr:
                nxt_arr.append(node.left)
                nxt_arr.append(node.right)
            dfs(currlv + 1, nxt_arr)

        dfs(0, [root])
        return root