"""
64 ms runtime beats 52.1%
16 MB memory beats 94%
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        def bfs(node):
            if not node:
                return
            q = deque([node])
            while q:
                tmp = []
                for _ in range(len(q)):
                    curr = q.popleft()
                    for o in curr.children:
                        q.append(o)
                    tmp.append(curr.val)
                res.append(tmp)
        
        res = []
        bfs(root)
        return res