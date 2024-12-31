"""
593 ms runtime beats 25.19%
25.72 MB memory beats 5.34%
"""
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Topological Sort, kahn's algorithm
        # dict: {element: index_order of element}
        ridx = self.tpsort(rowConditions, k)
        if len(ridx) < k:
            return []
        cidx = self.tpsort(colConditions, k)
        if len(cidx) < k:
            return []

        res = [[0] * k for _ in range(k)]
        for a in range(1, k + 1):
            res[ridx[a]][cidx[a]] = a
        return res

    def tpsort(self, arr, n):
        g = defaultdict(set)
        indegree = [0] * (n + 1)
        seen = set()
        for u, v in arr:
            if (u, v) not in seen:
                seen.add((u, v))
                g[u].add(v)
                indegree[v] += 1
        
        q = deque([i for i in range(1, n + 1) if indegree[i] == 0])
        dic = dict()
        while q:
            curr = q.popleft()
            # node's order by index
            dic[curr] = len(dic)
            for adj in g[curr]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
        return dic
