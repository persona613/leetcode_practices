"""
929 ms runtime beats 81.01%
50.20 MB memory beats 54.09%
"""
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        def dfs(node):
            ans = 0
            for neighbor in g[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        ans += 1
                    seen.add(neighbor)
                    ans += dfs(neighbor)
            return ans

        g = defaultdict(list)
        roads = set()
        for a, b in connections:
            g[a].append(b)
            g[b].append(a)
            roads.add((a, b))

        seen = {0}
        return dfs(0)
