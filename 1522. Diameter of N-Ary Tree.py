"""
42 ms runtime beats 73.94%
18.04 MB memory beats 71.83%
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        # return: node max height
        def dfs(node):
            nonlocal ans
            if not node.children:
                return 0
            if len(node.children) == 1:
                h = dfs(node.children[0])
                ans = max(ans, 1 + h)
                return 1+ h

            # max 2 children height
            mx1 = mx2 = 0
            for chi in node.children:
                h = dfs(chi)
                if h > mx1:
                    mx2 = mx1
                    mx1 = h
                elif h > mx2:
                    mx2 = h

            ans = max(ans, 2 + mx1 + mx2)
            return 1 + mx1

        ans = 0
        dfs(root)
        return ans