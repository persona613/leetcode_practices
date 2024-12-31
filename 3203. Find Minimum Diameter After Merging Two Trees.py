"""
407 ms runtime beats 84.83%
79.73 MB memory beats 83.45%
"""
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        # return (farest nodes and edges count)
        def bfs(tree, start):
            q = [start]
            seen = [False] * len(tree)
            seen[start] = True
            count = 0
            while q:
                nxt_level = []
                for curr in q:
                    for adj in tree[curr]:
                        if seen[adj] is False:
                            seen[adj] = True
                            nxt_level.append(adj)

                if not nxt_level:
                    break
                q = nxt_level
                count += 1
            return (q, count)

        def diameter(tree):
            nodes, _ = bfs(tree, 0)
            if not nodes:
                return 0
            _, count = bfs(tree, nodes[0])
            return count

        def build_tree(edges):
            g = [[] for _ in range(len(edges) + 1)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            return g

        tree1 = build_tree(edges1)
        tree2 = build_tree(edges2)
        d1 = diameter(tree1)
        d2 = diameter(tree2)
        d3 = (d1 + 1) // 2 + (d2 + 1) // 2 + 1
        return max(d1, d2, d3)