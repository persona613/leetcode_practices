"""
Wrong Answer
61 / 84 testcases passed

Editorial
Input
n =
9
edges =
[[2,3],[4,0],[3,1],[2,4],[0,1],[5,2],[6,5],[8,6],[7,8]]

Use Testcase
Output
[0,0,0,0,0,1,1,2,1]
Expected
[0,0,0,0,0,1,2,4,3]
"""
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        # try topological sort
        degree = [0] * n
        g = defaultdict(list)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            g[u].append(v)
            g[v].append(u)
        # init nodes with degree is 1
        q = deque()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)

        # topological sort path
        path = deque()
        # record pre-node of each node, cycle nodes have no pre-node
        pre = [None] * n
        while q:
            curr = q.popleft()
            degree[curr] -= 1
            path.appendleft(curr)
            # curr has only one edge
            for adj in g[curr]:
                degree[adj] -= 1
                pre[curr] = adj
                if degree[adj] == 1:
                    q.append(adj)

        # calculate distance from cycle 
        dist = [0] * n
        for node in path:
            pre_node = pre[node]
            dist[node] = dist[pre_node] + 1
        return dist