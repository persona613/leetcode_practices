"""
84 ms runtime beats 15.80%
16.92 MB memory beats 34.57%
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def dfs(st, path):
            if len(path) == n + 1:
                return True

            for nxt in adj[st]:
                if gf[st][nxt] > 0:
                    path.append(nxt)
                    gf[st][nxt] -= 1
                    if dfs(nxt, path):
                        return True
                    path.pop()
                    gf[st][nxt] += 1

        n = len(tickets)
        gf = defaultdict(lambda: defaultdict(int))
        for u, v in tickets:
            gf[u][v] += 1

        # adjcity list sorted
        # defaultdict for cities those out-degree is 0
        adj = defaultdict(list)
        for city in gf:
            adj[city] = sorted(gf[city].keys())
        
        path = ["JFK"]
        dfs("JFK", path)
        return path