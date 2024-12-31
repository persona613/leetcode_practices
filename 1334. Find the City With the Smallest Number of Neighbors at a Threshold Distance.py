"""
445 ms runtime beats 53.72%
17.79 MB memory beats 60.27%
"""
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # build matrix graph, row=from_node, col=to_node, val=weight
        mat = [[inf] * n for _ in range(n)]
        # init self node weight
        for i in range(n):
            mat[i][i] = 0
        for u, v, w in edges:
            mat[u][v] = w
            mat[v][u] = w
        
        # k is intermediate node for all pair(i, j)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        
        # {adj cities count: [node idx,]}
        dic = defaultdict(list)
        for i in range(n):
            cnt = sum(cost <= distanceThreshold for cost in mat[i])
            dic[cnt].append(i)
        mi = min(dic)
        return max(dic[mi])
        