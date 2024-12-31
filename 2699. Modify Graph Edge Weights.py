"""
2132 ms runtime beats 79.07%
20.46 MB memory beats 19.77%
"""
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:

        def dijkstra(graph, start, dest, temp_weight):
            path_cost = [float("inf")] * n
            path_cost[start] = 0
            # record path by first reach [pre_node_index]
            path_node = [-1] * n
            path_node[start] = start

            # min heap
            q = [(0, start)]
            while q:
                curr_cost, curr_node = heappop(q)
                if curr_node == dest:
                    break
                for adj in graph[curr_node]:
                    weight, edge_index = graph[curr_node][adj]
                    if weight < 0:
                        weight = temp_weight
                    if curr_cost + weight < path_cost[adj]:
                        path_cost[adj] = curr_cost + weight
                        path_node[adj] = curr_node
                        heappush(q, (path_cost[adj], adj))

            # path decode
            path = [dest]
            curr = dest
            while curr != start:
                pre = path_node[curr]
                path.append(pre)
                curr = pre
            return path_cost[dest], path[::-1]

        MIN = 1
        MAX = 2 * (10 ** 9)
        e = len(edges)
        # get modify_edges indexs
        modify_edges = set()
        for i in range(e):
            if edges[i][2] == -1:
                modify_edges.add(i)

        # build graph
        g = defaultdict(dict)
        for i in range(e):
            u, v, w = edges[i]
            g[u][v] = [w, i]
            g[v][u] = [w, i]

        # get shortest path's cost and path_edges with MAX weight
        # exclude impossible condition
        cost, path = dijkstra(g, source, destination, MAX)
        if cost < target:
            return []
        elif cost == target:
            for idx in modify_edges:
                edges[idx][2] = MAX
            return edges

        # get cost and path with MIN weight
        # find modify_edges_in_path(as meip)
        # iterate meip as mid edge and adjust its' weight
        cost, path = dijkstra(g, source, destination, MIN)
        for i in range(len(path) - 1):
            st = path[i]
            nd = path[i + 1]
            mid_index = g[st][nd][1]
            if mid_index in modify_edges:
                cost1, path1 = dijkstra(g, source, st, MAX)
                cost2, path2 = dijkstra(g, nd, destination, MAX)
                if cost1 + cost2 < target:
                    remain = target - cost1 - cost2
                    edges[mid_index][2] = remain
                    g[st][nd][0] = remain
                    g[nd][st][0] = remain
                    break
                else:
                    edges[mid_index][2] = MIN
                    g[st][nd][0] = MIN
                    g[nd][st][0] = MIN
        # no meip
        else:
            return []

        for idx in modify_edges:
            if edges[idx][2] == -1:
                edges[idx][2] = MAX
        return edges