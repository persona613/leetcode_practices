"""
554 ms runtime beats 27.07%
24.48 MB memory beats 38.69%
"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # topological sort
        indegree = [len(lst) for lst in graph]
        g = defaultdict(list)
        q = deque()
        for i, lst in enumerate(graph):
            if len(lst) == 0:
                q.append(i)
                continue
            for v in lst:
                g[v].append(i)

        res = list(q)
        while q:
            curr = q.popleft()
            for adj in g[curr]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
                    res.append(adj)
        return sorted(res)