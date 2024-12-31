"""
129 ms runtime beats 65.85%
40.05 MB memory beats 12.20%
"""
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        # return sum % k
        def dfs(node):
            curr = values[node] % k
            for adj in g[node]:
                if seen[adj] is False:
                    seen[adj] = True
                    curr = (curr + dfs(adj)) % k
                    
            # sum divisible
            if curr == 0:
                ans[0] += 1
            return curr
        
        seen = [False] * n
        seen[0] = True
        ans = [0]
        dfs(0)
        return ans[0]