"""
51 ms runtime beats 25.47%
17.49 MB memory beats 15.09%
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # parent to child order
        # return [increase length, decrease length]
        def dfs(node):
            nonlocal maxi
            if not node:
                return [0, 0]
            if not node.left and not node.right:
                return [1, 1]

            l = dfs(node.left)
            r = dfs(node.right)

            l_state = [False, False]
            r_state = [False, False]
            curr = node.val
            if node.left:
                # increase
                if curr + 1 == node.left.val:
                    l_state[0] = True
                    l[0] += 1
                else:
                    l[0] = 1
                # decrease
                if curr - 1 == node.left.val:
                    l_state[1] = True
                    l[1] += 1
                else:
                    l[1] = 1
            if node.right:
                if curr + 1 == node.right.val:
                    r_state[0] = True
                    r[0] += 1
                else:
                    r[0] = 1
                if curr - 1 == node.right.val:
                    r_state[1] = True
                    r[1] += 1
                else:
                    r[1] = 1

            curr_maxi = max(*l, *r)
            # check child-parent-child order
            if l_state[0] and r_state[1]:
                curr_maxi = max(curr_maxi, l[0] + r[1] - 1)
            elif l_state[1] and r_state[0]:
                curr_maxi = max(curr_maxi, l[1] + r[0] - 1)
            if curr_maxi > maxi:
                maxi = curr_maxi
            return [max(l[0], r[0]), max(l[1], r[1])]

        maxi = 1
        dfs(root)
        return maxi