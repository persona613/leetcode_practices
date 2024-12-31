"""
134 ms runtime beats 90.20%
50.40 MB memory beats 18.95%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def count_sort(values):
            arr_sorted = sorted(values)
            dic = dict()
            for i, v in enumerate(values):
                dic[v] = i

            steps = 0
            for i in range(len(values)):
                if values[i] != arr_sorted[i]:
                    target_pos = dic[arr_sorted[i]]
                    dic[values[i]] = target_pos
                    # dic[arr_sorted[i]] = i
                    values[i], values[target_pos] = values[target_pos], values[i]
                    steps += 1
            return steps

        steps = 0
        q = deque([root])
        while q:
            n = len(q)
            values = []
            for _ in range(n):
                curr = q.popleft()
                values.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            steps += count_sort(values)
        return steps