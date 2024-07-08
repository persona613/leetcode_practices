"""
176 ms runtime beats 96.39%
17.63 MB memory beats 61.45%
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node):
            for neighbor in g[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        n = len(isConnected)
        g = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    g[i].append(j)
                    g[j].append(i)
        ans = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        return ans