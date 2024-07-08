"""
250 ms runtime beats 85.17%
22.44 MB memory beats 12.74%
"""
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def dfs(node, seen, path):
            seen[node] = True
            path[node] = True
            # end node is not dest
            if node not in gf:
                return False
            
            for nxt in gf[node]:
                if nxt == destination:
                    continue
                if seen[nxt] is False:
                    if dfs(nxt, seen, path) == False:
                        return False
                elif path[nxt] is True: # detect cycle
                    return False

            # backtracing path stack
            path[node] = False
            return True

        # set for parallel edges
        gf = defaultdict(set)
        for u, v in edges:
            gf[u].add(v)

        if source == destination and source not in gf:
            return True
        # dest have no out-going edges
        if destination in gf or source not in gf:
            return False

        seen = [False] * n
        path = [False] * n
        return dfs(source, seen, path)