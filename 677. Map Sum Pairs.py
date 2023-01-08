"""
93 ms runtime beats 6.29%
14 MB memory beats 76.70%
"""
class TrieNode:
    def __init__(self, val=0):
        self.children = {}
        self.val = val
        self.isend = False

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.val = val
        curr.isend = True

    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return self.bfs(curr)
    
    def bfs(self, node):
        q = deque([node])
        res = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                q.extend(curr.children.values())
                if curr.isend:
                    res += curr.val
        return res
                    
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)