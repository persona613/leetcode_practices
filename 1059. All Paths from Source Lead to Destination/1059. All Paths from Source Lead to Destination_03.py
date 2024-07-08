"""
Time Limit Exceeded
55 / 57 testcases passed
submitted at May 14, 2024 04:15

Editorial
Last Executed Input
Use Testcase
n =
100
"""
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def dfs(node):
            if node not in gf:
                return False
            
            for nxt in gf[node]:
                if nxt == destination:
                    continue
                if nxt in seen:
                    return False
                seen.add(nxt)
                if dfs(nxt) == False:
                    return False
                seen.remove(nxt)
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

        seen = {source}
        return dfs(source)