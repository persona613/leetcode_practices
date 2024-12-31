"""
141 ms runtime beats 82.78%
17.51 MB memory beats 7.75%
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # paint curr_node and check adjs' color
        def dfs(node, color):
            if marks[node] >= 0:
                return marks[node] == color

            marks[node] = color
            bicolor = True
            for adj in graph[node]:
                if not dfs(adj, color ^ 1):
                    bicolor = False
            return bicolor

        n = len(graph)
        # two colors of nodes [0, 1]
        marks = [-1] * n

        # all disjoint graph should bipartite
        bipartite = True
        for i in range(n):
            if marks[i] < 0:
                if not dfs(i, 0):
                    bipartite = False
        return bipartite