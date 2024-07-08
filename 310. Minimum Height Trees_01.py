"""
845 ms runtime beats 12.41%
31.67 MB memory beats 5.76%
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # find leaf nodes
        def bfs(root):
            q = deque([root])
            while q:
                bag = []
                for curr in q:
                    for adj in gf[curr]:
                        if adj not in seen:
                            seen.add(adj)
                            bag.append(adj)
                if not bag:
                    return q
                q = bag

        # find diameter path
        def dfs(curr, target):
            if curr == target:
                return [target]

            for adj in gf[curr]:
                if adj not in seen:
                    seen.add(adj)
                    ret = dfs(adj, target)
                    if ret:
                        return ret + [curr]

        # create graph
        gf = [[] for _ in range(n)]
        for u, v in edges:
            gf[u].append(v)
            gf[v].append(u)

        # first bfs to find leaf-nodes, start from random node
        seen = {0}
        leaves = bfs(0)
        start = leaves[0]
        # second bfs to find diameter nodes
        seen = {start}
        ends = bfs(start)

        # find diameter path
        seen = {start}
        path = dfs(start, ends[0])
        ln = len(path)
        if ln % 2:
            return [path[ln // 2]]
        else:
            return path[ln // 2 - 1: ln // 2 + 1]