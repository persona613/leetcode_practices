"""
Runtime: 90 ms, faster than 9.83% of Python3 online submissions 
Memory Usage: 14.5 MB, less than 0% of Python3 online submissions
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        seen = defaultdict(Node)
        
        
        def srch(node):
            if node.val not in seen:
                new = Node(node.val)
                seen[node.val] = new
            else:
                return seen[node.val]
            
            for n in node.neighbors :
                new.neighbors.append(srch(n))
                
            return new

        return srch(node)