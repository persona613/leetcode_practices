"""
Wrong Answer
51 / 57 testcases passed
submitted at May 14, 2024 03:52

Editorial
Input
n =
5
edges =
[[0,1],[0,2],[0,3],[0,3],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
source =
0
destination =
4

Use Testcase
Output
false
Expected
true
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
            return True

        # set for parallel edges
        gf = defaultdict(set)
        for u, v in edges:
            gf[u].add(v)

        # dest have no out-going edges
        if destination in gf or source not in gf:
            return False

        seen = {source}
        return dfs(source)