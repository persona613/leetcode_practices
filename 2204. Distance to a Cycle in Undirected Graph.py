"""
100 ms runtime beats 92.05%
69.80 MB memory beats 55.26%
"""
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        # try topological sort
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        # init nodes with degree is 1
        q = deque()
        for i in range(n):
            if len(g[i]) == 1:
                q.append(i)

        # topological sort path
        path = deque()
        # record pre-node of each node, cycle nodes have no pre-node
        pre = [None] * n
        while q:
            curr = q.popleft()
            path.appendleft(curr)

            # curr has only one edge
            adj = g[curr].pop()
            g[adj].remove(curr)
            if len(g[adj]) == 1:
                q.append(adj)

            # record pre node
            pre[curr] = adj

        # calculate distance from cycle 
        dist = [0] * n
        for node in path:
            pre_node = pre[node]
            dist[node] = dist[pre_node] + 1
        return dist