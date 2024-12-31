"""
Wrong Answer
38 / 39 testcases passed

Editorial
Input
pairs =
[[3,2],[5,1],[1,0],[2,3],[0,2],[2,5]]

Use Testcase
Output
[[3,2],[5,1],[1,0],[2,3],[0,2],[2,5]]
Expected
[[3,2],[2,5],[5,1],[1,0],[0,2],[2,3]]
"""
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        
        # try Hierholzer’s algorithm modified with edges instead of nodes
        def dfs(edges):
            while edges:
                nxt_edge = edges.pop()
                dfs(adj[nxt_edge[1]])
                res.append(nxt_edge)

        # node: [in-Degree, out-Degree]
        deg = defaultdict(lambda: [0, 0])
        # node: out-edges
        adj = defaultdict(list)
        for edge in pairs:
            u, v = edge
            # out
            deg[u][1] += 1
            # in
            deg[v][0] += 1
            adj[u].append(edge)

        # find star node: out-Degree - in-Degree == 1
        start = -1
        for node, cnt in deg.items():
            if cnt[1] - cnt[0] == 1:
                start = node
                break
        # all nodes have out-D - in-D == 0, any node could be start
        if start == -1:
            return pairs

        res = []
        dfs(adj[start])
        return res[::-1]