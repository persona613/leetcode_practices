"""
396 ms runtime beats 79.23%
26.30 MB memory beats 81.28%
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]

        # try khan's algorithm
        degree = [0] * n
        gf = [[] for _ in range(n)]
        for u, v in edges:
            gf[u].append(v)
            gf[v].append(u)
            degree[u] += 1
            degree[v] += 1

        q = deque([i for i in range(n) if degree[i] == 1])
        while q:
            size = len(q)
            tmp = []
            for _ in range(size):
                curr = q.popleft()
                degree[curr] -= 1
                tmp.append(curr)
                for adj in gf[curr]:
                    if degree[adj]: # pass parent node
                        degree[adj] -= 1
                        if degree[adj] == 1:
                            q.append(adj)
        return tmp